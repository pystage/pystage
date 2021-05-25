'''
Rules:
    - Every template ends at the indent_level where it started.
    - At the end of block code add a blank line.
    - New functions add a newline at the beginning to get to 2 blank lines.
'''

def event_whenflagclicked(writer, block):
    writer.newline()
    writer.write(f"def program_start_{writer.get_id()}(self):")
    writer.indent_level += 1
    writer.newline()
    writer.write_next_or_pass(block)
    writer.indent_level -= 1
    writer.newline(1)
    writer.write(f"{writer.get_sprite_var()}.when_program_is_started(program_start_{writer.last_id})")
    writer.newline(1)

def event_broadcast(w, b):
    w.write_line(f'broadcast({b.params.BROADCAST_INPUT})')

def event_whenbroadcastreceived(w, b):
    w.write_line(f'def message_received_{w.get_id()}(self):', 1, -1)
    w.indent_level += 1
    w.newline()
    w.write_next_or_pass(b)
    w.indent_level -= 1
    w.write_line(f'{w.get_sprite_var()}.when_i_receive_message({b.params.BROADCAST_OPTION}, message_received_{w.last_id})', 2, 1)

def motion_setx(w,b):
    w.write_line(f"self.set_x_to({w.get_ex(b.params.X)})")


def motion_xposition(w,b):
    w.write(f"self.get_x()")


def motion_movesteps(w,b):
    w.write_line(f"self.move({w.get_ex(b.params.STEPS)})")


def event_whenkeypressed(w, b):
    w.write_block(f'''\
            
            def key_pressed_{w.get_id()}(self):
                {w.get_next_or_pass(b,4)}
                
                
            {w.get_sprite_var()}.when_key_is_pressed({b.params.KEY_OPTION}, key_pressed_{w.last_id})
            
            ''')

def data_setvariableto(w,b):
    w.write_line(f'self.set_global_variable({b.params.VARIABLE}, {w.get_ex(b.params.VALUE)})')

def control_repeat_until(w,b):
    w.write_line(f'while not {w.get_ex(b.params.CONDITION)}:', 1, -1)
    w.indent_level += 1
    w.newline()
    w.ex_or_pass(b.params.SUBSTACK)
    w.indent_level -= 1
    w.newline()

def control_if(w,b):
    w.write_line(f'if {w.get_ex(b.params.CONDITION)}:', 1, -1)
    w.indent_level += 1
    w.newline()
    w.ex_or_pass(b.params.SUBSTACK)
    w.indent_level -= 1
    w.newline()


def operator_equals(w,b):
    w.write(f'{w.get_ex(b.params.OPERAND1)} == {w.get_ex(b.params.OPERAND2)}')

def operator_lt(w,b):
    w.write(f'{w.get_ex(b.params.OPERAND1)} < {w.get_ex(b.params.OPERAND2)}')

def operator_gt(w,b):
    w.write(f'{w.get_ex(b.params.OPERAND1)} > {w.get_ex(b.params.OPERAND2)}')

def operator_and(w,b):
    w.write(f'({w.get_ex(b.params.OPERAND1)} and {w.get_ex(b.params.OPERAND2)})')

def operator_or(w,b):
    w.write(f'({w.get_ex(b.params.OPERAND1)} or {w.get_ex(b.params.OPERAND2)})')

def operator_subtract(w,b):
    w.write(f'({w.get_ex(b.params.NUM1)} - {w.get_ex(b.params.NUM2)})')
