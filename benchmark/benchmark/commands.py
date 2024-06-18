from os.path import join

from benchmark.utils import PathMaker


class CommandMaker:

    @staticmethod
    def cleanup_configs():
        return f'rm -f *.yaml'

    @staticmethod
    def make_logs_dir(ts):
        return f'mkdir -p {PathMaker.logs_path(ts)}'
        
    @staticmethod
    def compile():
        return 'go build -o node ../main.go'

    @staticmethod
    def run_config():
        return f'go run ../config_gen/main.go'
    
    @staticmethod
    def run_node(config_file):
        return (f'./node --config {config_file}')

    @staticmethod
    def kill():
        return 'tmux kill-server'
