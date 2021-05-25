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
    writer.next_or_pass(block)
    writer.indent_level -= 1
    writer.newline(3)
    writer.write(f"{writer.get_sprite_var()}.when_program_is_started(program_start_{writer.last_id})")
    writer.newline(2)

