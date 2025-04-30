from setuptools import setup, find_packages

setup(
    name='spark_tts',  # 可以自定义一个名字
    version='0.1.0',
    description='fork from SparkAudio/Spark-TTS',
    author='kongyatong',
    author_email='yatong.kong@gmail.com',
    packages=find_packages(),  # 自动找到所有含 __init__.py 的目录
    install_requires=[
        line.strip()
        for line in open("requirements.txt").readlines()
        if line.strip() and not line.startswith("#")
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            # 如果你的包里有可执行脚本入口，比如：
            # 'your_command = your_package.main:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
