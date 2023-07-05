# switchbackdrop (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('basketball_2')
stage.add_backdrop('pool')
stage.create_variable('my variable', 0)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(-41)
sprite1.set_y(-51)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_backdrop_switches_to_1(self):
    self.move(100.0)

sprite1.when_backdrop_switches_to("basketball_2", when_backdrop_switches_to_1)

def when_program_starts_2(self):
    self.switch_backdrop_to("pool")
    self.wait(1.0)
    self.next_backdrop()

sprite1.when_program_starts(when_program_starts_2)
stage.play()
