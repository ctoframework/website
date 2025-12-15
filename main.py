from pathlib import Path
import yaml

def define_env(env):

    @env.macro
    def load_page_yaml(filename):
        page = env.page
        md_path = Path(page.file.abs_src_path)
        data_path = md_path.parent / filename

        with data_path.open() as f:
            return yaml.safe_load(f)
