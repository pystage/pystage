'''
Rules:
    - Every template ends at the indent_level where it started.
    - At the end of block code add a blank line.
    - New functions (hat blocks) add a newline at the beginning to get to 2 blank lines.
'''

templates = {
        "control_if": '''\
                if {{CONDITION}}:
                    {{SUBSTACK | indent(4)}}
                ''',
        
        "event_whenflagclicked": '''\
                
                def program_start_{{ID}}(self):
                    {{NEXT | indent(4) }}

                {{CURRENT_SPRITE}}.when_program_is_started(program_start_{{ID}})

                ''',
        
        "event_whenbroadcastreceived": '''\

                def message_received_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.when_i_receive_message({{BROADCAST_OPTION}}, message_received_{{ID}})

                ''',

        "event_whenkeypressed": '''\

                def key_pressed_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.when_key_is_pressed({{KEY_OPTION}}, key_pressed_{{ID}})
                
                ''',

        "control_repeat_until": '''\
                while not {{CONDITION}}:
                    {{SUBSTACK | indent(4)}}
                ''',

        "control_if": '''\
                if {{CONDITION}}:
                    {{SUBSTACK | indent(4)}}
                ''',

        "operator_equals": "{{OPERAND1}} == {{OPERAND2}}",

        "operator_lt": "{{OPERAND1}} < {{OPERAND2}}",

        "operator_gt": "{{OPERAND1}} > {{OPERAND2}}",

        "operator_and": "{{OPERAND1}} and {{OPERAND2}}",

        "operator_or": "{{OPERAND1}} or {{OPERAND2}}",

        "operator_subtract": "{{NUM1}} - {{NUM2}}",

        "operator_add": "{{NUM1}} + {{NUM2}}",

        "looks_costume": "{{COSTUME | global_costume}}",

        "looks_backdrops": "{{BACKDROP | global_backdrop}}",

        "sound_sounds_menu": "{{SOUND_MENU | global_sound }}",

                }


