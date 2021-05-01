from multiprocessing import Process
import control
import camera

if __name__ == "__main__":
    control_p = Process(target=control.start)
    camera_p = Process(target=camera.start)
    control_p.start()
    camera_p.start()