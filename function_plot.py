import input_signals as isig
import matplotlib.pyplot as plt
import numpy as np
import output_signals as osig




def generate_input_signal(self):
    print("Generating input signal")

    if self.feSenoide_button.isChecked():
        a0 = self.feAmplitud_text.text()
        f0 = self.feFrecuencia_text.text()

        if a0 != '' and f0 != '' and float(a0) > 0 and float(f0) > 0:
            # self.update_input_plot(self)
            isig.input_signal.tt, isig.input_signal.st = isig.generate_sinusoidal_signal(100, float(f0), 10000, float(a0), 0)
            #plot input signal with matplotlib
            print("Plotting input signal")


            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(isig.input_signal.tt, isig.input_signal.st)
            self.MplWidget.canvas.axes.legend("Entrada")
            self.MplWidget.canvas.draw()

            osig.test(self)

        else:
            print("Clearing input signal plot")
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.draw()



    elif self.feEscalon_button.isChecked():
        a0 = self.feAmplitud_text.text()

        if a0 != '' and float(a0) > 0:
            # self.update_input_plot(self)
            input_signal = isig.generate_step_signal(100, 100, float(a0))
            #plot input signal with matplotlib
            print("Plotting input signal")
            tt, st = input_signal


            # self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(tt, st)
            self.MplWidget.canvas.axes.legend("En")
            self.MplWidget.canvas.draw()
        else:
            print("Clearing input signal plot")
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.draw()


    elif self.fePulso_button.isChecked():

        a0 = self.feAmplitud_text.text()
        f0 = self.feFrecuencia_text.text()

        if a0 != '' and f0 != '' and float(a0) > 0 and float(f0) > 0:
            # self.update_input_plot(self)
            input_signal = isig.generate_square_signal(100, float(f0), 100, float(a0), 0, 0.5)
            #plot input signal with matplotlib
            print("Plotting input signal")
            tt, st = input_signal

            # self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(tt, st)
            self.MplWidget.canvas.axes.legend("En")
            self.MplWidget.canvas.draw()

        else:
            print("Clearing input signal plot")
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.draw()

