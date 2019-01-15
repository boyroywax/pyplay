***
# Lamden Python Blockchain Playground
***
- Launch Python based Blockchain using Lamden Python Open Source Blockchain discovered in [TalkPython Episode 165: Python and the Blockchain](https://talkpython.fm/episodes/show/165/python-and-the-blockchain)
  - [Lamden Whitepaper](https://blog.lamden.io/a-complete-overview-of-the-lamden-suite-2eb43c730b40)


## Software Used in this project:
- Mac OSX 10.14.2
- Anaconda Python 3.7.2 Env
- Docker

***
### Lamden - Seneca Smart Contract
***
[Lamden Docs: Installing Seneca Locally](https://docs.lamden.io/seneca/getting-started/installing-locally)
- Requires Redis
- Jupyter Notebook recomended IDE
- MACOSX: install unittest with homebrew EDIT: LOL I realize this is unnessary now, because it is built into Python
  ```
  brew install unittest
  ```
  

***
### Lamden - Cilantro Blockchain
***
[Cilantro Github Repo](https://github.com/Lamden/cilantro)

#### Installing using conda python 3.7 environment workaround:

- [Install pycapnp manually on MACOSX with XCODE Installed](https://github.com/capnproto/pycapnp)
```
CFLAGS='-stdlib=libc++' pip install pycapnp
```
#### Install Cilantro
- Download Cilantro and dependencies
```
git clone https://github.com/Lamden/cilantro.git
cd/to/cilantro
pip install -r requirements.txt
mkdir logs
```
- [install mongodb on macosx](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/#install-mongodb-community-edition)