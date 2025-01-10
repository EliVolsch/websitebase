from jinja2 import Environment, FileSystemLoader

def environment(**options):
    # Define the loader explicitly
    options['loader'] = FileSystemLoader('templates')  # Load templates from the 'templates' directory
    env = Environment(**options)  # Pass options (which now includes the loader)
    return env
