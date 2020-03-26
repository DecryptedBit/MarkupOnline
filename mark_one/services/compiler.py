from threading import Thread
import pypandoc

def async_compiler(md_string, dest):
    output = pypandoc.convert_text(md_string, 'pdf', 
                format='md', outputfile=dest, 
                extra_args=['--mathjax',])
    
    return output

def compile_md(md_string, dest):
    thread = Thread(target=async_compiler, args=[md_string, dest])
    thread.start()
