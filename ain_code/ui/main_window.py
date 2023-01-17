# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1038, 779)
        MainWindow.setStyleSheet("#frame, #frame_2, #frame_4{\n"
"    border: 1px solid black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(290, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.two_pd_radioButton = QtWidgets.QRadioButton(self.frame)
        self.two_pd_radioButton.setChecked(True)
        self.two_pd_radioButton.setObjectName("two_pd_radioButton")
        self.horizontalLayout_2.addWidget(self.two_pd_radioButton)
        self.n_pd_radioButton = QtWidgets.QRadioButton(self.frame)
        self.n_pd_radioButton.setObjectName("n_pd_radioButton")
        self.horizontalLayout_2.addWidget(self.n_pd_radioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout.addWidget(self.label_19)
        self.n_spinBox = QtWidgets.QSpinBox(self.frame)
        self.n_spinBox.setMinimum(3)
        self.n_spinBox.setMaximum(20)
        self.n_spinBox.setProperty("value", 4)
        self.n_spinBox.setObjectName("n_spinBox")
        self.horizontalLayout.addWidget(self.n_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("#frame_3{border: 1px solid black}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cd_uno_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.cd_uno_spinBox.setMaximum(200)
        self.cd_uno_spinBox.setObjectName("cd_uno_spinBox")
        self.gridLayout.addWidget(self.cd_uno_spinBox, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.dc_uno_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.dc_uno_spinBox.setMaximum(200)
        self.dc_uno_spinBox.setProperty("value", 50)
        self.dc_uno_spinBox.setObjectName("dc_uno_spinBox")
        self.gridLayout.addWidget(self.dc_uno_spinBox, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.cc_uno_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.cc_uno_spinBox.setMaximum(200)
        self.cc_uno_spinBox.setProperty("value", 30)
        self.cc_uno_spinBox.setObjectName("cc_uno_spinBox")
        self.gridLayout.addWidget(self.cc_uno_spinBox, 0, 1, 1, 1)
        self.dd_uno_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.dd_uno_spinBox.setMaximum(200)
        self.dd_uno_spinBox.setProperty("value", 10)
        self.dd_uno_spinBox.setObjectName("dd_uno_spinBox")
        self.gridLayout.addWidget(self.dd_uno_spinBox, 3, 1, 1, 1)
        self.cc_dos_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.cc_dos_spinBox.setMaximum(200)
        self.cc_dos_spinBox.setProperty("value", 30)
        self.cc_dos_spinBox.setObjectName("cc_dos_spinBox")
        self.gridLayout.addWidget(self.cc_dos_spinBox, 0, 2, 1, 1)
        self.cd_dos_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.cd_dos_spinBox.setMaximum(200)
        self.cd_dos_spinBox.setProperty("value", 50)
        self.cd_dos_spinBox.setObjectName("cd_dos_spinBox")
        self.gridLayout.addWidget(self.cd_dos_spinBox, 1, 2, 1, 1)
        self.dc_dos_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.dc_dos_spinBox.setMaximum(200)
        self.dc_dos_spinBox.setObjectName("dc_dos_spinBox")
        self.gridLayout.addWidget(self.dc_dos_spinBox, 2, 2, 1, 1)
        self.dd_dos_spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.dd_dos_spinBox.setMaximum(200)
        self.dd_dos_spinBox.setProperty("value", 10)
        self.dd_dos_spinBox.setObjectName("dd_dos_spinBox")
        self.gridLayout.addWidget(self.dd_dos_spinBox, 3, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.num_of_tournaments_spinBox = QtWidgets.QSpinBox(self.frame)
        self.num_of_tournaments_spinBox.setMinimum(1)
        self.num_of_tournaments_spinBox.setMaximum(1000)
        self.num_of_tournaments_spinBox.setProperty("value", 151)
        self.num_of_tournaments_spinBox.setObjectName("num_of_tournaments_spinBox")
        self.gridLayout_2.addWidget(self.num_of_tournaments_spinBox, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)
        self.prob_of_init_c_spinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.prob_of_init_c_spinBox.setDecimals(2)
        self.prob_of_init_c_spinBox.setMaximum(1.0)
        self.prob_of_init_c_spinBox.setSingleStep(0.01)
        self.prob_of_init_c_spinBox.setProperty("value", 0.5)
        self.prob_of_init_c_spinBox.setObjectName("prob_of_init_c_spinBox")
        self.gridLayout_2.addWidget(self.prob_of_init_c_spinBox, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.num_of_opponents_spinBox = QtWidgets.QSpinBox(self.frame)
        self.num_of_opponents_spinBox.setMinimum(1)
        self.num_of_opponents_spinBox.setMaximum(1000)
        self.num_of_opponents_spinBox.setProperty("value", 10)
        self.num_of_opponents_spinBox.setObjectName("num_of_opponents_spinBox")
        self.gridLayout_2.addWidget(self.num_of_opponents_spinBox, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.prehistory_l_spinBox = QtWidgets.QSpinBox(self.frame)
        self.prehistory_l_spinBox.setMinimum(1)
        self.prehistory_l_spinBox.setMaximum(6)
        self.prehistory_l_spinBox.setProperty("value", 3)
        self.prehistory_l_spinBox.setObjectName("prehistory_l_spinBox")
        self.gridLayout_2.addWidget(self.prehistory_l_spinBox, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_4.addWidget(self.frame)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(290, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pop_size_spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.pop_size_spinBox.setMinimum(2)
        self.pop_size_spinBox.setMaximum(999999999)
        self.pop_size_spinBox.setProperty("value", 100)
        self.pop_size_spinBox.setObjectName("pop_size_spinBox")
        self.gridLayout_3.addWidget(self.pop_size_spinBox, 0, 1, 1, 1)
        self.mutation_prob_spinBox = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.mutation_prob_spinBox.setDecimals(3)
        self.mutation_prob_spinBox.setMaximum(1.0)
        self.mutation_prob_spinBox.setProperty("value", 0.003)
        self.mutation_prob_spinBox.setObjectName("mutation_prob_spinBox")
        self.gridLayout_3.addWidget(self.mutation_prob_spinBox, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.num_of_gener_spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.num_of_gener_spinBox.setMinimum(1)
        self.num_of_gener_spinBox.setMaximum(999999999)
        self.num_of_gener_spinBox.setProperty("value", 200)
        self.num_of_gener_spinBox.setObjectName("num_of_gener_spinBox")
        self.gridLayout_3.addWidget(self.num_of_gener_spinBox, 1, 1, 1, 1)
        self.crossover_prob_spinBox = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.crossover_prob_spinBox.setDecimals(2)
        self.crossover_prob_spinBox.setMaximum(1.0)
        self.crossover_prob_spinBox.setSingleStep(0.01)
        self.crossover_prob_spinBox.setProperty("value", 0.9)
        self.crossover_prob_spinBox.setObjectName("crossover_prob_spinBox")
        self.gridLayout_3.addWidget(self.crossover_prob_spinBox, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.tournament_size_spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.tournament_size_spinBox.setMinimum(2)
        self.tournament_size_spinBox.setMaximum(999999999)
        self.tournament_size_spinBox.setProperty("value", 3)
        self.tournament_size_spinBox.setObjectName("tournament_size_spinBox")
        self.gridLayout_3.addWidget(self.tournament_size_spinBox, 2, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.frame_2)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.elitist_strategy_checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.elitist_strategy_checkBox.setObjectName("elitist_strategy_checkBox")
        self.verticalLayout_2.addWidget(self.elitist_strategy_checkBox)
        self.verticalLayout_4.addWidget(self.frame_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(290, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.seed_line = QtWidgets.QLineEdit(self.frame_4)
        self.seed_line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.seed_line.setInputMask("")
        self.seed_line.setText("")
        self.seed_line.setObjectName("seed_line")
        self.horizontalLayout_4.addWidget(self.seed_line)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.num_of_runs_spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.num_of_runs_spinBox.setMinimum(1)
        self.num_of_runs_spinBox.setMaximum(999999999)
        self.num_of_runs_spinBox.setObjectName("num_of_runs_spinBox")
        self.horizontalLayout_3.addWidget(self.num_of_runs_spinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_6.addWidget(self.label_17)
        self.freq_gen_start_spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.freq_gen_start_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.freq_gen_start_spinBox.setMinimum(1)
        self.freq_gen_start_spinBox.setMaximum(1000)
        self.freq_gen_start_spinBox.setProperty("value", 30)
        self.freq_gen_start_spinBox.setObjectName("freq_gen_start_spinBox")
        self.horizontalLayout_6.addWidget(self.freq_gen_start_spinBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.delta_freq_spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.delta_freq_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.delta_freq_spinBox.setMinimum(1)
        self.delta_freq_spinBox.setMaximum(200)
        self.delta_freq_spinBox.setProperty("value", 10)
        self.delta_freq_spinBox.setObjectName("delta_freq_spinBox")
        self.horizontalLayout_6.addWidget(self.delta_freq_spinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addWidget(self.frame_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.debug_checkBox = QtWidgets.QCheckBox(self.widget)
        self.debug_checkBox.setObjectName("debug_checkBox")
        self.horizontalLayout_5.addWidget(self.debug_checkBox, 0, QtCore.Qt.AlignHCenter)
        self.load_checkBox = QtWidgets.QCheckBox(self.widget)
        self.load_checkBox.setObjectName("load_checkBox")
        self.horizontalLayout_5.addWidget(self.load_checkBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.run_button = QtWidgets.QPushButton(self.widget)
        self.run_button.setMinimumSize(QtCore.QSize(160, 40))
        self.run_button.setMaximumSize(QtCore.QSize(160, 16777215))
        self.run_button.setObjectName("run_button")
        self.verticalLayout_5.addWidget(self.run_button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.widget)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_7.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.avg_frame = QtWidgets.QFrame(self.centralwidget)
        self.avg_frame.setMinimumSize(QtCore.QSize(500, 300))
        self.avg_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.avg_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avg_frame.setObjectName("avg_frame")
        self.verticalLayout_3.addWidget(self.avg_frame)
        self.freq_frame = QtWidgets.QFrame(self.centralwidget)
        self.freq_frame.setMinimumSize(QtCore.QSize(500, 300))
        self.freq_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.freq_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.freq_frame.setObjectName("freq_frame")
        self.verticalLayout_3.addWidget(self.freq_frame)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prisoners dilemma"))
        self.label.setText(_translate("MainWindow", "Pd game params"))
        self.two_pd_radioButton.setText(_translate("MainWindow", "2_PD"))
        self.n_pd_radioButton.setText(_translate("MainWindow", "N_PD"))
        self.label_19.setText(_translate("MainWindow", "N"))
        self.label_2.setText(_translate("MainWindow", "2p PD payoff function"))
        self.label_6.setText(_translate("MainWindow", "DD"))
        self.label_4.setText(_translate("MainWindow", "CD"))
        self.label_3.setText(_translate("MainWindow", "CC"))
        self.label_5.setText(_translate("MainWindow", "DC"))
        self.label_20.setText(_translate("MainWindow", "prob_of_init_C"))
        self.label_8.setText(_translate("MainWindow", "num_of_opponents"))
        self.label_7.setText(_translate("MainWindow", "num_of_tournaments"))
        self.label_9.setText(_translate("MainWindow", "prehistory L"))
        self.label_10.setText(_translate("MainWindow", "GA parameters"))
        self.label_11.setText(_translate("MainWindow", "pop_size"))
        self.label_12.setText(_translate("MainWindow", "torunament_size"))
        self.label_14.setText(_translate("MainWindow", "mutation_prob"))
        self.label_13.setText(_translate("MainWindow", "num_of_gener"))
        self.label_32.setText(_translate("MainWindow", "crossover_prob"))
        self.elitist_strategy_checkBox.setText(_translate("MainWindow", "elitist_strategy"))
        self.label_15.setText(_translate("MainWindow", "Seed"))
        self.label_16.setText(_translate("MainWindow", "num_of_runs"))
        self.label_17.setText(_translate("MainWindow", "freq_gen_start"))
        self.label_18.setText(_translate("MainWindow", "delta_freq"))
        self.debug_checkBox.setText(_translate("MainWindow", "debug"))
        self.load_checkBox.setText(_translate("MainWindow", "LOAD DATA"))
        self.run_button.setText(_translate("MainWindow", "RUN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
