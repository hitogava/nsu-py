from setuptools import Extension, setup

setup(
    name="foreign",
    version="1.0.0",
    description="Python interface for printing something from C",
    author="123",
    author_email="1234",
    ext_modules=[
        Extension(
            name="foreign",
            sources=["tiny14.c"],
        ),
    ]
)
