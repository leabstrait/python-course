prog_langs = {}

prog_langs = {
    'python':       'interpreted, high level, general purpose, dynamically typed, object oriented, functional',
    'c':            'compiled, high level, general purpose, system programming, statically typed, procedural',
    'c++':          'compiled, high level, general purpose, graphics programming, statically typed, object oriented, functional',
    'assembly':     'machine, low level, architecture specific, sequential',
    'javascript':   'interpreted, JIT compiled, high level, general purpose, dynamically typed, functional, prototypal object oriented',
    'java':         'compiled to VM JVM, high level, general purpose, statically typed, object oriented, functional',
    'c#':           'compiled to VM CLR, high level, general purpose, statically typed, object oriented, functional',
    'lisp':         'interpreted, high level, general purpose, dynamically typed, functional',
    'erlang':       'compiled to VM BEAM, high level, concurrent systems, dynamically typed, functional'
}

# print(prog_langs)

# keys values items

# for lang in prog_langs.keys():
#     print(lang)

# for lang_description in prog_langs.values():
#     print(lang_description)

# for lang, lang_desc in prog_langs.items():
#     print(lang, ':')
#     print(lang_desc)
#     print()



prog_langs_breakdown = {
    'python': {
        'execution_type': 'interpreted',
        'abstraction':    'high level',
        'purpose':        ['general purpose'],
        'type system':    'dynamically typed',
        'paradigms':      ['object oriented', 'functional']
    },
    'c': {
        'execution_type': 'compiled',
        'abstraction':    'high level',
        'purpose':        ['general purpose', 'system programming'],
        'type system':    'statically typed',
        'paradigms':      ['procedural']
    },
    'c++': {
        'execution_type': 'compiled',
        'abstraction':    'high level',
        'purpose':        ['general purpose', 'graphics programming'],
        'type system':    'statically typed',
        'paradigms':      ['object oriented', 'functional']
    },
    'assembly': {
        'execution_type': 'machine',
        'abstraction':    ['low level', 'architecture specific'],
        'purpose':        ['system programming', 'compilers'],
        'type system':    '',
        'paradigms':      ['sequential']
    },
    'javascript': {
        'execution_type': ['interpreted', 'JIT compiled'],
        'abstraction':    'high level',
        'purpose':        'general purpose',
        'type system':    'dynamically typed',
        'paradigms':      ['prototypal object oriented', 'functional']
    }
}


prog_langs_breakdown['assembly']['purpose'].append('embedded systems')

# print(prog_langs_breakdown['assembly']['purpose'])

# prog_langs['html'] = 'not really a programming language'

# for lang in sorted(prog_langs):
#     print(lang, ':',prog_langs[lang])

print(prog_langs.get('python'))
print(prog_langs.get('ruby'))

prog_langs.update({'ruby':'a funny language', 'groovy':'a funny language in JVM'})

print(prog_langs.get('ruby'))

prog_langs.pop('ruby')
print(prog_langs.get('ruby'))
print(prog_langs.get('groovy'))


help(dict)