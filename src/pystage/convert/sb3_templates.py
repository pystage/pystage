'''
Rules:
    - Every template ends at the indent_level where it started.
    - At the end of block code add a blank line.
    - New functions (hat blocks) add a newline at the beginning to get to 2 blank lines.
'''

templates = {
        
        "event_whenflagclicked": '''\
                
                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4) }}

                {{CURRENT_SPRITE}}.{{func}}({{func}}_{{ID}})

                ''',
        
        "event_whenbroadcastreceived": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{BROADCAST_OPTION}}, {{func}}_{{ID}})

                ''',

        "event_whenkeypressed": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{KEY_OPTION}}, {{func}}_{{ID}})
                
                ''',

        "event_whenthisspriteclicked": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{func}}_{{ID}})
                
                ''',
                
        "control_start_as_clone": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{func}}_{{ID}})
                
                ''',

        "control_forever":'''\
                while True:
                    {{SUBSTACK | indent(4)}}
                ''',

        "control_repeat":'''\
                for _ in range({{TIMES}}):
                    {{SUBSTACK | indent(4)}}
                ''',

        "control_repeat_until": '''\
                while not {{CONDITION}}:
                    {{SUBSTACK | indent(4)}}
                ''',
        
        "control_wait_until": '''\
                while not {{CONDITION}}:
                    pass
                ''',

        "control_if": '''\
                if {{CONDITION}}:
                    {{SUBSTACK | indent(4)}}
                ''',

        "control_if_else":'''\
                if {{CONDITION}}:
                    {{SUBSTACK | indent(4)}}
                else:
                    {{SUBSTACK2 | indent(4)}}
                ''',

        "operator_add": "({{NUM1}} + {{NUM2}})",
        "operator_and": "({{OPERAND1}} and {{OPERAND2}})",
        "operator_contains": "({{STRING2}} in {{STRING1}})",
        "operator_divide": "({{NUM1}} / {{NUM2}})",
        "operator_equals": "({{OPERAND1}} == {{OPERAND2}})",
        "operator_gt": "({{OPERAND1}} > {{OPERAND2}})",
        "operator_join": '"".join([{{STRING1}}, {{STRING2}}])',
        "operator_length": "len({{STRING}})",
        "operator_letter_of": "{{STRING}}[{{LETTER}}-1]",
        "operator_lt": "({{OPERAND1}} < {{OPERAND2}})",
        "operator_mod": "({{NUM1}} % {{NUM2}})",
        "operator_multiply": "({{NUM1}} * {{NUM2}})",
        "operator_not": "not ({{OPERAND}})",
        "operator_or": "({{OPERAND1}} or {{OPERAND2}})",
        "operator_round": "round({{NUM}})",
        "operator_subtract": "({{NUM1}} - {{NUM2}})",

        "looks_costume": "{{COSTUME | global_costume}}",
        "looks_backdrops": "{{BACKDROP | global_backdrop}}",
        "sound_sounds_menu": "{{SOUND_MENU | global_sound }}",

                }


