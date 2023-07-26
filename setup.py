import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def take_package_name(name):
    if name.startswith("-e"):
        return name[name.find("=")+1:name.rfind("-")]
    else:
        return name.strip()


def load_requires_from_file(filepath):
    with open(filepath) as fp:
        return [take_package_name(pkg_name) for pkg_name in fp.readlines()]


def load_links_from_file(filepath):
    res = []
    with open(filepath) as fp:
        for pkg_name in fp.readlines():
            if pkg_name.startswith("-e"):
                res.append(pkg_name.split(" ")[1])
    return res


setuptools.setup(
    name="sungonTest",
    version="0.0.5",
    author="sungon",
    author_email="sungon.lee@encored.co.jp",
    description="ejhelper is lib for encored japan development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sungonlee/package-management",
    download_url='https://github.com/sungonlee/package-management/blob/main/dist/sungonTest-0.0.5.tar.gz',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.7",
)