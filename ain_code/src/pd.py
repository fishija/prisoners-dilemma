from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QRegExp

from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,  QDialog, QLabel, QComboBox, QMessageBox, QHeaderView, QTreeWidgetItem, QWidget, QVBoxLayout, QTreeWidget, QCheckBox, QHBoxLayout
from PyQt5.QtCore import QThread, Qt, QAbstractTableModel, QCoreApplication, QSize, QThreadPool
from PyQt5.QtGui import QPixmap

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from ui.main_window import Ui_MainWindow

from src.classes import GameWorker

import matplotlib
import pandas as pd
import random
import sys


matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class PDWindow(Ui_MainWindow, QMainWindow):
    # Pd game params
    two_pd = False
    n_pd = False
    n_players = 0
    two_pd_payoff_func = dict(cc_uno = 0, cc_dos = 0, cd_uno = 0, cd_dos = 0, dc_uno = 0, dc_dos = 0, dd_uno = 0, dd_dos = 0)
    prob_of_init_c = 0
    num_of_tournaments = 0
    num_of_opponents = 0
    prehistory_l = 0

    # GA params
    pop_size = 0
    num_of_gener = 0
    tournament_size = 0
    crossover_prob = 0
    mutation_prob = 0
    elitist_strategy = False

    # Other params
    seed = 0
    num_of_runs = 0
    debug = False

    # Params to present data
    avg_data_per_generation = pd.DataFrame(columns=['Avg per Gen', 'Avg per Best'])
    # history_count_per_gen = pd.DataFrame(columns=[])
    

    def __init__(self):
        super(PDWindow, self). __init__()

        self.setupUi(self)

        # set seed input validator
        self.seed_line.setValidator(QRegExpValidator(QRegExp(r'\d+')))

        # connect run button
        self.run_button.clicked.connect(self.run)

        self.show()

    def set_attributes(self):
        # Pd game params
        self.two_pd = self.two_pd_radioButton.isChecked()
        self.n_pd = self.n_pd_radioButton.isChecked()
        self.n_players = self.n_spinBox.value()
        self.prob_of_init_c = self.prob_of_init_c_spinBox.value()
        self.num_of_tournaments = self.num_of_tournaments_spinBox.value()
        self.num_of_opponents = self.num_of_opponents_spinBox.value()
        self.prehistory_l = self.prehistory_l_spinBox.value()

        self.two_pd_payoff_func['cc_uno'] = self.cc_uno_spinBox.value()
        # self.two_pd_payoff_func['cc_dos'] = self.cc_dos_spinBox.value()
        self.two_pd_payoff_func['cd_uno'] = self.cd_uno_spinBox.value()
        # self.two_pd_payoff_func['cd_dos'] = self.cd_dos_spinBox.value()
        self.two_pd_payoff_func['dc_uno'] = self.dc_uno_spinBox.value()
        # self.two_pd_payoff_func['dc_dos'] = self.dc_dos_spinBox.value()
        self.two_pd_payoff_func['dd_uno'] = self.dd_uno_spinBox.value()
        # self.two_pd_payoff_func['dd_dos'] = self.dd_dos_spinBox.value()

        # GA params
        self.pop_size = self.pop_size_spinBox.value()
        self.num_of_gener = self.num_of_gener_spinBox.value()
        self.tournament_size = self.tournament_size_spinBox.value()
        self.crossover_prob = self.crossover_prob_spinBox.value()
        self.mutation_prob = self.mutation_prob_spinBox.value()
        self.elitist_strategy_checkBox.isChecked()

        # Other params
        if self.seed_line.text() == '':
            self.seed = random.randint(0, sys.maxsize)
        else:
            self.seed = float(self.seed_line.text())

        self.num_of_runs = self.num_of_runs_spinBox.value()
        self.debug = self.debug_checkBox.isChecked()

    def input_valid(self):
        # cd_uno/dc_dos < dd_uno/dd_dos < cc_uno/cc_dos < dc_uno/cd_uno

        cc_uno, cc_dos = (self.cc_uno_spinBox.value(), self.cc_dos_spinBox.value())
        cd_uno, cd_dos = (self.cd_uno_spinBox.value(), self.cd_dos_spinBox.value())
        dc_uno, dc_dos = (self.dc_uno_spinBox.value(), self.dc_dos_spinBox.value())
        dd_uno, dd_dos = (self.dd_uno_spinBox.value(), self.dd_dos_spinBox.value())

        if self.two_pd:
            if not dc_uno > cc_uno or not dc_uno > cc_dos or\
               not cd_dos > cc_uno or not cd_dos > cc_dos or\
               not cc_uno > dd_uno or not cc_uno > dd_dos or\
               not cc_dos > dd_uno or not cc_dos > dd_dos or\
               not dd_uno > cd_uno or not dd_uno > dc_dos or\
               not dd_dos > cd_uno or not dd_dos > dc_dos:

                QMessageBox.warning(self, '2p PD payoff func ERROR', 'Data in 2p PD payoff function has to look like:\n\nCD_left/DC_right < DD_left/DD_right < CC_left/CC_right < DC_left/CD_left')
                return False
        return True

    def thread_finished(self):
        # Unlock app
        self.run_button.setEnabled(True)
        print(self.avg_data_per_generation)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.avg_data_per_generation.plot(ax=sc.axes)

        layout = QVBoxLayout()
        layout.addWidget(sc)

        self.avg_widget.setLayout(layout)


    def update_upper_plot(self, avg_gen: float, avg_best: float):
        print(avg_gen, avg_best)
        self.avg_data_per_generation.loc[len(self.avg_data_per_generation)] = [avg_gen, avg_best]
        pass

    def update_lower_plot(self, history_count: list):
        # print(history_count)
        pass
                
    def run(self):
        if self.input_valid():
            # Clean plots!!!!!!!!!!!!!!!!!!!!!!!!!!


            # Lock app
            self.run_button.setDisabled(True)


            self.set_attributes()



            self.threadpool = QThreadPool()
            self.worker = GameWorker(self.two_pd, 
                                    self.n_players, 
                                    self.two_pd_payoff_func, 
                                    self.prob_of_init_c, 
                                    self.num_of_tournaments, 
                                    self.num_of_opponents,
                                    self.prehistory_l,
                                    self.pop_size,
                                    self.num_of_gener,
                                    self.tournament_size,
                                    self.crossover_prob,
                                    self.mutation_prob,
                                    self.elitist_strategy,
                                    self.seed,
                                    self.debug)

            self.worker.signals.finished.connect(self.thread_finished)
            self.worker.signals.avg_progress.connect(self.update_upper_plot)
            self.worker.signals.updated_history_count.connect(self.update_lower_plot)
            self.threadpool.start(self.worker)
