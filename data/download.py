from subprocess import check_output
import time

for n in range(265, 545):
    check_output(
        f'curl -o {n}.pdf https://twblg.dict.edu.tw/holodict_new/iongji/pdf/annesia{n}pdf.pdf',
        shell=True)
    time.sleep(1)
