import sys
from GUI import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIntValidator, QIcon, QPainter, QPainterPath, QKeySequence, QMovie
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from get_twitch_profile_icon import *
from sentimental_analysis import Sentiment_Analysis
from encoding_module import encoding_song
from rnn_model import training_model,build_Note_model,build_Chord_model
from midi_generator import generator
from utils import *

import pandas as pd
import os
import socket
import shutil
import random
#initialized
my_app_id = "2cycuwui7dpel8ifi37kekgi7pc2xm"
my_app_secret = "zexwnwnif9x79hwoiuryd9qr3no7f6"
app = QApplication([])
streamerID = ''
data_range = ''
bpm = ''
midi_ins = [0, 0, 0, 0]
error = 0
chatlog = ''
end = False
file_num = 0
x, y = 0, 0
emotion="positive"
instrument = ''
current_file=''


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        global emotion
        # Window setting
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.setWindowTitle("Sentiment analysis-based music generator")
        self.setWindowIcon(QIcon('logo.ico'))
        self.btn_Exit.clicked.connect(self.close)
        self.btn_Min.clicked.connect(self.showMinimized)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.icon_twitch.setPixmap(self.circleImg("assets/twitch_profile.jpg"))
        self.Twitch_icon_Option.setPixmap(self.circleImg("assets/Twitch.png"))
        self.shortcut = QShortcut(QKeySequence("Shift+Esc"), self)
        self.shortcut.activated.connect(app.quit)
        # Page tab setting(pushbutton)
        self.btn_File_Browser.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.btn_Option.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_ChatnPlayer.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        
        # Edit setting
        self.edit_datarange.setValidator(QIntValidator(0, 100))
        self.edit_BPM.setValidator(QIntValidator(1, 300))
        self.tEdit_Chatlog.setReadOnly(True)
        self._streamerThread = streamerThread(self)
        self.edit_ChannelID.editingFinished.connect(self.getstreamerID)
        self.edit_ChannelID.editingFinished.connect(self._streamerThread.start)
        self._streamerThread.updated.connect(self.setStreamerImg_Error)
        self._streamerThread.finished.connect(self.setstreamerimg)
        # Confirm button
        self.btn_Confirm_Option.clicked.connect(self.optionconfirm)
        
        #Train button
        self._gif=QMovie('assets/loading.gif')
        self.gif_loading.setMovie(self._gif)
        self.gif_loading.setVisible(False)
        self.label_training.setText('')
        self._trainThread = trainThread(self)
        self.btn_train.clicked.connect(self._trainThread.start)
        self.btn_train.clicked.connect(self.whiletraining)
        self._trainThread.finished.connect(self.trainingfinished)
        
        # Chat setting(run Thread)
        self._botThread = BotThread(self)
        self._botThread.updated.connect(self.updateText)
        self.btn_chat.clicked.connect(self._botThread.start)
        self.btn_chat.clicked.connect(self.btn_chat.hide)
        self._botThread.finished.connect(self.finishedThread)
        self._botThread.finished.connect(self.inputaudiofile)
        self._botThread.emote.connect(self.showemotion)
        
        
        #File setting
        self.rbtn_pos.clicked.connect(
            lambda: self.createfilewidget("positive"))
        self.rbtn_neu.clicked.connect(
            lambda: self.createfilewidget("neutral"))
        self.rbtn_neg.clicked.connect(
            lambda: self.createfilewidget("negative"))
        self.createfilewidget("positive")
        self.btn_import_file.clicked.connect(self.appendwidget)
        self.btn_refresh.clicked.connect(lambda:self.createfilewidget(emotion))
        self.btn_clear.clicked.connect(lambda:self.clearfile(emotion))
        
        
        #Media setting
        self.btn_Play.setEnabled(False)
        self.btn_Next.setEnabled(False)
        self.btn_Pre.setEnabled(False)
        self.icon_play = QtGui.QIcon()
        self.icon_play.addPixmap(QtGui.QPixmap(":/Icons/assets/play_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_pause = QtGui.QIcon()
        self.icon_pause.addPixmap(QtGui.QPixmap(":/Icons/assets/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.state = "Play"
        self.playlist = []
        self.position = 0
        self.index=""
        self.player=QMediaPlayer()
        self.inputaudiofile()
        self.btn_Play.clicked.connect(self.play_button)
        self.Audio_Slider.sliderMoved.connect(self.set_postition)
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.music_list.clicked.connect(self.set_state)
        self.btn_Next.clicked.connect(self.skip_forward)
        self.btn_Pre.clicked.connect(self.skip_backward)
        self.btn_delete_track.clicked.connect(self.deletetrack)
    #Show Loading
    def whiletraining(self):
        self._gif.start()
        self.gif_loading.setVisible(True)
        self.label_training.setText('Model Training...')
        self.rbtn_neg.setEnabled(False)
        self.rbtn_pos.setEnabled(False)
        self.rbtn_neu.setEnabled(False)
        self.btn_train.setEnabled(False)
        self.btn_clear.setEnabled(False)
        self.btn_import_file.setEnabled(False)
        self.btn_refresh.setEnabled(False)
        self.scrollArea.setEnabled(False)
    def trainingfinished(self):
        self._gif.stop()
        self.gif_loading.setVisible(False)
        self.label_training.setText('Training Success')
        self.rbtn_neg.setEnabled(True)
        self.rbtn_pos.setEnabled(True)
        self.rbtn_neu.setEnabled(True)
        self.btn_train.setEnabled(True)
        self.btn_clear.setEnabled(True)
        self.btn_import_file.setEnabled(True)
        self.btn_refresh.setEnabled(True)
        self.scrollArea.setEnabled(True)
        
    #ChatEmotion
    def showemotion(self,emote):
        self.PageTitle_Chat.setText("Chat - " + emote)
        
    #Audio player
    def deletetrack(self):
        global current_file
        if current_file!="":
            name = 'audio_output/'+current_file
            os.remove(name)
            self.inputaudiofile()
        
    def skip_backward(self):
        try:
            self.music_list.setCurrentRow(self.index - 1)
            self.play_audio()
        except:
            pass
    def skip_forward(self):
        try:
            self.music_list.setCurrentRow(self.index + 1)
            self.play_audio()
        except:
            pass
    def play_audio(self):
        global current_file
        self.btn_Play.setIcon(self.icon_pause)
        self.state = "Pause"
        self.btn_Play.setStatusTip("Pause")
        current_file=self.music_list.currentItem().text()
        path ="audio_output/"+  current_file
        print(current_file)
        if 'positive' in current_file:
            self.Background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.5, y2:1," 
                                          "stop:0 rgba(212, 144, 72, 255), stop:1 rgba(160, 255, 156, 255));"
                                          "border-radius:25px;")
        elif 'negative' in current_file:
            self.Background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.5, y2:1," 
                                          "stop:0 rgba(151, 112, 226, 255), stop:1 rgba(26, 80, 185, 255));"
                                          "border-radius:25px;")
        else:
            self.Background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.5, y2:1," 
                                          "stop:0 rgba(170, 97, 212, 255), stop:1 rgba(156, 194, 255, 255));"
                                          "border-radius:25px;")
        url = QUrl.fromLocalFile(path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.index= self.music_list.currentRow().__index__()
        self.player.setPosition(self.position)
        self.playlist.append(path)
        if len(self.playlist) > 2:
            self.playlist.pop(0)
        if path !=self.playlist[0]:
            self.position = 0
            self.player.setPosition(self.position)
        self.player.play()
    def set_state(self):
        self.btn_Play.setEnabled(True)
        self.btn_Next.setEnabled(True)
        self.btn_Pre.setEnabled(True)
        self.play_audio()
    def play_button(self):
        if self.state == "Play":
            # icon pause
            self.play_audio()
        elif self.state == "Pause":
            # icon play
            self.btn_Play.setIcon(self.icon_play)
            self.state = "Play"
            self.btn_Play.setStatusTip("Play")
            self.player.pause()
            paused = self.player.position()
            self.position = paused
    def set_postition(self,position):
        self.player.setPosition(position)
    def position_changed(self,position):
        self.Audio_Slider.setValue(position)
    def duration_changed(self, duration):
        self.Audio_Slider.setRange(0, duration)
    def inputaudiofile(self):
        self.music_list.clear()
        for root, dirs, files in os.walk('audio_output'):
            # select file name
            for file in files:
                self.music_list.addItem(file)
    #File Browser
    def createfilewidget(self,e):
        global emotion
        emotion=e
        x, y, c = 0, 0, 0
        self.destroyallwidget()
        for root, dirs, files in os.walk('midi_training/'+e):
            # select file name
            for file in files:
                if x == 4:
                    y += 1
                    x = 0
                # check the extension of files
                if file.endswith('.mid'):
                    # print whole path of files
                    path = os.path.join(file)
                    self.createwidget(y, x, path)
                    x += 1
                c+=1
        self.label_count.setText("Files Amount："+str(c))
        self.Title_Channel.setText("File Browser - "+e )
    def destroyallwidget(self):
        lc=list(range(self.gridLayout.count()))
        lc.reverse()
        for i in lc:
            item=self.gridLayout.itemAt(i)
            self.gridLayout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
            
    def clearfile(self,e):
        lc=list(range(self.gridLayout.count()))
        lc.reverse()
        for i in lc:
            file=self.gridLayout.itemAt(i).widget().objectName()
            name = 'midi_training/'+e+'/'+file
            item=self.gridLayout.itemAt(i)
            self.gridLayout.removeItem(item)
            os.remove(name)
            if item.widget():
                item.widget().deleteLater()
        self.createfilewidget(e)
        
    def appendwidget(self):
        v = self.gridLayout.count()
        filename, _ = QFileDialog.getOpenFileName(self, '開啟圖檔','./','Image Files(*.mid)')
        if filename:
            shutil.copy2(filename, 'midi_training/'+emotion)
        self.destroyallwidget()
        self.createfilewidget(emotion)

    def deletemidifile(self, file,e):
        name = 'midi_training/'+e+'/'+file
        os.remove(name)
        frame_name=file
        self.destroyallwidget()
        self.createfilewidget(e)
    def createwidget(self, rowNum, columNum, file):

        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(200, 200))
        self.frame.setMaximumSize(QtCore.QSize(200, 200))
        self.frame.setStatusTip(file)
        self.frame.setStyleSheet("QFrame{\n"
                                 "border:2px solid gray;\n"
                                 "border-radius:5px;\n"
                                 "}\n"
                                 "QFrame:hover{\n"
                                 "border:2px solid rgb(255, 255, 0);\n"
                                 "}\n"
                                 "QLabel{\n"
                                 "border:none;\n"
                                 "}\n"
                                 "QLabel:hover{\n"
                                 "border:none;\n"
                                 "}")
        Frame_name = file
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(Frame_name)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 100, 100))
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Icons/assets/file_alt2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(3, 120, 190, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setText(file)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 10, 40, 40))
        self.pushButton.setStyleSheet("border:none")
        self.pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(
            ":/Icons/assets/close_widget.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        btn_name = "btn_close_"+file
        self.pushButton.setObjectName(btn_name)
        self.pushButton.clicked.connect(lambda: self.deletemidifile(file,emotion))
        
        self.gridLayout.addWidget(
            self.frame, rowNum, columNum, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)

    # updateEditText with chatbot
    def updateText(self, text):
        self.tEdit_Chatlog.append(text)
        self.tEdit_Chatlog.setStyleSheet('''QTextEdit{border: 2px solid rgb(255, 255, 0);
										 background-color: qlineargradient(spread:pad, x1:0.483, y1:0, x2:0.5, y2:1, stop:0 rgba(85, 18, 123, 250), stop:1 rgba(0, 0, 0, 212));
										 color:#FFF;
										 font:150 16pt "微軟正黑體";
										 padding-left:20px;
										 padding-right:20px;}''')
    def finishedThread(self):
        self.btn_Option.setEnabled(True)
        self.tEdit_Chatlog.setStyleSheet('''QTextEdit{border-top: 2px solid rgb(162, 60, 206);
										 background-color: qlineargradient(spread:pad, x1:0.483, y1:0, x2:0.5, y2:1, stop:0 rgba(85, 18, 123, 250), stop:1 rgba(0, 0, 0, 212));
										 color:#FFF;
										 font:150 16pt "微軟正黑體";
										 padding-left:20px;
										 padding-right:20px;}''')
    # Option confirm
    def optionconfirm(self):
        global error
        self.id_error.setText("")
        self.data_error.setText("")
        self.bpm_error.setText("")
        self.id_error.setText("")
        self.midi_error.setText("")

        if self.btn_midi_piano.isChecked():
            midi_ins[0] = 1
        if self.btn_midi_saxphone.isChecked():
            midi_ins[1] = 1
        if self.btn_midi_trumpet.isChecked():
            midi_ins[2] = 1
        if self.btn_midi_guitar.isChecked():
            midi_ins[3] = 1

        if not self.edit_ChannelID.text():
            self.id_error.setText("Enter ID")
            error += 1
        if not self.edit_datarange.text():
            self.data_error.setText("Enter data range")
            error += 1
        if not self.edit_BPM.text():
            self.bpm_error.setText("Enter bpm")
            error += 1
        if midi_ins == [0, 0, 0, 0]:
            self.midi_error.setText("Choose instrument")
            error += 1

            
            
        if error == 0:
            global data_range, bpm,instrument
            data_range = int(self.edit_datarange.text())
            bpm = int(self.edit_BPM.text())
            self.icon_twitch.setPixmap(
            self.circleImg("profile_image/profile.png"))
            self.btn_ChatnPlayer.setChecked(True)
            self.stackedWidget.setCurrentWidget(self.page_3)
            self.btn_Option.setEnabled(False)
            self.tEdit_Chatlog.setText("")
            self.btn_chat.show()
            if self.btn_midi_guitar.isChecked():
                instrument = 'guitar'
            if self.btn_midi_piano.isChecked():
                instrument = 'piano'
            if self.btn_midi_saxphone.isChecked():
                instrument = 'saxphone'
            if self.btn_midi_trumpet.isChecked():
                instrument = 'trumpet'
            
    # Get StreamerID&img
    def setStreamerImg_Error(self):
        self.Twitch_icon_Option.setPixmap(
            self.circleImg("assets/Twitch.png"))
        self.id_error.setText("Streamer ID not found")
    
    def getstreamerID(self):
        global streamerID
        streamerID = self.edit_ChannelID.text()
    def setstreamerimg(self):
        global error
        if error == 0:
            self.Twitch_icon_Option.setPixmap(
                self.circleImg("profile_image/profile.png"))

    # Get circle icon
    def circleImg(self, imagepath):
        image = QPixmap(imagepath)
        size = min(image.width(), image.height())
        scaled = QPixmap(size, size)
        scaled.fill(Qt.transparent)

        painter = QPainter(scaled)
        painter.setRenderHints(painter.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        painter.setClipPath(path)

        rect = QRect(0, 0, size, size)
        rect.moveCenter(image.rect().center())
        painter.drawPixmap(scaled.rect(), image, rect)
        painter.end()
        return scaled
    
    # titlebar drag event
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        if(event.localPos().y() <= 50):
            delta = QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

#------------------------------------
# mutiThread for chatbot
class BotThread(QtCore.QThread):
    global emotion
    updated = QtCore.pyqtSignal(object)
    emote = QtCore.pyqtSignal(object)
    def run(self):
        global chatlog, end
        HOST = "irc.twitch.tv"
        PORT = 6667
        PASS = "oauth:9gx824bstrz6f4c5dt5a7ga9pemjez"
        BOTNICK = "chiladon022"
        BOTPASS = "oauth:9gx824bstrz6f4c5dt5a7ga9pemjez"
        list1 = []
        list2 = []
        list3 = []
        c = 0
        NICK = streamerID
        print("Bot is Running")
        sock = socket.socket()
        sock.connect((HOST, PORT))
        sock.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
        sock.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
        sock.send(bytes("JOIN #" + NICK + "\r\n", "UTF-8"))
        while True:
            line = str(sock.recv(2048))
            if "End of /NAMES list" in line:
                break

        while c <= data_range:
            for line in str(sock.recv(2048)).split('\\r\\n'):

                parts = line.split(':')
                if len(parts) < 3:
                    continue

                if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                    msg = parts[2][:len(parts[2])]

                usernamesplit = parts[1].split("!")
                username = usernamesplit[0]
                msg = msg.encode('ascii').decode(
                    'unicode-escape').encode('latin-1').decode('utf-8')
                username = username.encode().decode(encoding='UTF-8', errors='strict')
                print(c, end=" ")
                print(username + ": " + msg)
                chatlog = username + ": " + msg
                self.updated.emit(chatlog)
                if username != 'nightbot' or username !='streamelements':
                    list1.append(c)
                    list2.append(username)
                    list3.append(msg)
                    c += 1

                if c >= data_range:  # 聊天室資料筆數
                    break

        d = {'index': list1, 'user': list2, 'msg': list3}
        chat_df = pd.DataFrame(data=d)
        print(chat_df)
        chat_df.to_csv("msg.csv", index=False, encoding='UTF-8')
        chatlog = ''
        a = Sentiment_Analysis()
        s=0
        if a[0] == 0:
            emotion = 'negative'
            self.emote.emit(emotion)
            x = 0
            for root, dirs, files in os.walk('weights/negative/'):
                # select file name
                for file in files:
                    x+=1
            c = random.randint(0,(x/2-1))
            s=c
            Note_model = build_Note_model(emotion,s,weights_path='weights/negative/Note_weights'+str(c)+'.hdf5')
            Chord_model = build_Chord_model(emotion,s,weights_path='weights/negative/Chord_weights'+str(c)+'.hdf5')
            Note_corpus_path = 'Note_corpus/negative/Note_corpus_'+str(c)+'.bin'
            Note_voca_path = 'Note_voca/negative/Note_voca_'+str(c)+'.json'
            Chord_corpus_path = 'Chord_corpus/negative/Chord_corpus_'+str(c)+'.bin'
            Chord_voca_path = 'Chord_voca/negative/Chord_voca_'+str(c)+'.json'
            
        elif a[0] == 1:
            emotion = 'neutral'
            self.emote.emit(emotion)
            x = 0
            for root, dirs, files in os.walk('weights/neutral/'):
                # select file name
                for file in files:
                    x+=1
            c = random.randint(0,(x/2-1))
            s=c
            Note_model = build_Note_model(emotion,s,weights_path='weights/neutral/Note_weights'+str(c)+'.hdf5')
            Chord_model = build_Chord_model(emotion,s,weights_path='weights/neutral/Chord_weights'+str(c)+'.hdf5')
            Note_corpus_path = 'Note_corpus/neutral/Note_corpus_'+str(c)+'.bin'
            Note_voca_path = 'Note_voca/neutral/Note_voca_'+str(c)+'.json'
            Chord_corpus_path = 'Chord_corpus/neutral/Chord_corpus_'+str(c)+'.bin'
            Chord_voca_path = 'Chord_voca/neutral/Chord_voca_'+str(c)+'.json'
        elif a[0] == 2:
            emotion = 'positive'
            self.emote.emit(emotion)
            x = 0
            for root, dirs, files in os.walk('weights/positive/'):
                # select file name
                for file in files:
                    x+=1
            c = random.randint(0,(x/2-1))
            s=c
            Note_model = build_Note_model(emotion,s,weights_path='weights/positive/Note_weights'+str(c)+'.hdf5')
            Chord_model = build_Chord_model(emotion,s,weights_path='weights/positive/Chord_weights'+str(c)+'.hdf5')
            Note_corpus_path = 'Note_corpus/positive/Note_corpus_'+str(c)+'.bin'
            Note_voca_path = 'Note_voca/positive/Note_voca_'+str(c)+'.json'
            Chord_corpus_path = 'Chord_corpus/positive/Chord_corpus_'+str(c)+'.bin'
            Chord_voca_path = 'Chord_voca/positive/Chord_voca_'+str(c)+'.json'
            
        print(instrument)
        generator(Note_model,Chord_model,instrument,bpm,emotion,s)
        
        
        
        self.finished.emit()

class trainThread(QtCore.QThread):
    global emotion
    def run(self):
        x = 0
        
        for root, dirs, files in os.walk('Note_corpus/'+emotion):
            # select file name
            for file in files:
                x+=1
        a = random.randint(0,x)
        path = 'midi_training/'+emotion
        weight = 'weights/'+emotion
        encoding_song(path,emotion)
        training_model(a,weight,emotion)
        
    
    
        self.finished.emit()


class streamerThread(QtCore.QThread):
    updated = QtCore.pyqtSignal(object)

    def run(self):
        global streamerID, error
        error = 0
        temp = get_twitch_user(my_app_id, my_app_secret, streamerID)
        if temp == "":
            error += 1
            self.updated.emit(self)
        else:
            error = 0
        self.finished.emit()





if __name__ == "__main__":

    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
