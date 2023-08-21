import openai
import streamlit as st

programming_languages = (
            "python", "abap", "abc", "actionscript", "ada", "alda", "apache_conf", "apex", "applescript", "aql", 
            "asciidoc", "asl", "assembly_x86", "autohotkey", "batchfile", "c9search", "c_cpp", "cirru", 
            "clojure", "cobol", "coffee", "coldfusion", "crystal", "csharp", "csound_document", "csound_orchestra", 
            "csound_score", "csp", "css", "curly", "d", "dart", "diff", "django", "dockerfile", "dot", "drools", 
            "edifact", "eiffel", "ejs", "elixir", "elm", "erlang", "forth", "fortran", "fsharp", "fsl", "ftl", 
            "gcode", "gherkin", "gitignore", "glsl", "gobstones", "golang", "graphqlschema", "groovy", "haml", 
            "handlebars", "haskell", "haskell_cabal", "haxe", "hjson", "html", "html_elixir", "html_ruby", "ini", 
            "io", "jack", "jade", "java", "javascript", "json", "json5", "jsoniq", "jsp", "jssm", "jsx", "julia", 
            "kotlin", "latex", "less", "liquid", "lisp", "livescript", "logiql", "logtalk", "lsl", "lua", "luapage", 
            "lucene", "makefile", "markdown", "mask", "matlab", "maze", "mediawiki", "mel", "mixal", "mushcode", 
            "mysql", "nginx", "nim", "nix", "nsis", "nunjucks", "objectivec", "ocaml", "pascal", "perl", "perl6", 
            "pgsql", "php", "pig", "plain_text", "powershell", "praat", "prisma", "prolog", 
            "properties", "protobuf", "puppet", "qml", "r", "razor", "rdoc", "red", "redshift", "rhtml", 
            "rst", "ruby", "rust", "sass", "scad", "scala", "scheme", "scss", "sh", "sjs", "slim", "smarty", 
            "snippets", "soy_template", "space", "sparql", "sql", "sqlserver", "stylus", "svg", "swift", "tcl", 
            "terraform", "toml", "tsx", "turtle", "twig", "typescript", "vala", "vbscript", 
            "xml", "xquery", "yaml"
            )

model_details = {
    'Davinci':'text-davinci-003',
    'GPT-3.5':'gpt-3.5-turbo',
    'GPT-4':'gpt-4'
}

action_details = {
    'translate': 'Traducir',
    'code_explanation': 'Explicar',
    'bug_fix': 'Corregir'
}


output_results = {
    'Explicar': ('Lenguaje Natural',),
    'Corregir': ('Corregir Código',),
    'Traducir': programming_languages
}

prompts_configuration = [
    {'translate': "Por favor convierta el código delimitado con tres tildes invertidas del código {0} a {1}:\n '''{2}''' \n '''{1}"},
    {'bug_fix': "Verifique el código {0} delimitado con tres tildes invertidas para ver si hay errores y proporcione una solución: \n'''{1}''' "},
    {'code_explanation': "Por favor proporcione una explicación en lenguaje sencillo para el código {0} delimitado con triples acentos graves:\n '''{1}'''"}
]

def define_prompt(action, input_language, code, output_language=False):
    prompt = "" 

    if action == 'Traducir':
        prompt = prompts_configuration[0]['translate'].format(input_language, output_language, code)
    elif action == 'Corregir':
        prompt = prompts_configuration[1]['bug_fix'].format(input_language, code)
    elif action == 'Explicar':
        prompt = prompts_configuration[2]['code_explanation'].format(input_language, code)

    return prompt


def request(model, prompt):
    r = openai.ChatCompletion.create(
        model=model,
        messages=[
            {'role':'system', 'content':"Eres un programador experto, la herramienta de desarrollo de IA más avanzada del planeta. Incluso cuando no estás familiarizado con la respuesta, usas tu extrema inteligencia para descifrarla."},
            {'role':'user', 'content': prompt}
            ],
        temperature=0,
    )

    return r.choices[0]['message']['content']