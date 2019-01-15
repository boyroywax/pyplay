# PyPlay - Personal Testing Playground for Discord Bots
Abstract: testing pyton 3.7, mysql, json import, rpc calls for crypto, email, aysnc/await

## Goal
Build Discord Tip Bot from scratch with Python3.7 and asyncio

## Planned Features:
- Kubernetes managed Cryptocurrency TipBot Cluster
- Email 2FA
- Standard Wallet Funcions
- Coin/Chain Swap Ready
- Social Tipping Features: Rain, Soak, Games, ETC.

## Examples of asyncio discord bots
- [GridCoin Discord Bot (Python 3.7 & mySQL)](https://gitlab.com/delta1512/grc-wallet-bot)

## Tools Used
- Version Control: boyroywax [GitHub](https://github.com/boyroywax/pyplay)
- Local Virtual Env for testing: Anaconda (conda)
- Coding Language: Python 3.7.2
- GUI Editor: Microsoft Visual Studio Code
- Testing Framework: pytest package
- Asyncio Concurrent Development
- Logging: logging module
- f. strings
- Database: MySQL
- Web Dashboard: Django
- Chat Interface: [Discord.py](https://discordpy.readthedocs.io/en/latest/migrating.html)
- HTTP and REST: Requests package
- Container: Docker + Kubernetes for management
- Continuous Integration: Travis
- minikube - https://github.com/kubernetes/minikube

## Process
1. Update Discord Bot Core to Asyncio Python 3.7



***
## Future Projects
***
- Launch Python based Blockchain using Lamden Python Open Source Blockchain discovered in [TalkPython Episode 165: Python and the Blockchain](https://talkpython.fm/episodes/show/165/python-and-the-blockchain)
  - [Lamden Whitepaper](https://blog.lamden.io/a-complete-overview-of-the-lamden-suite-2eb43c730b40)

***
### Lamden - Seneca Smart Contract
***
[Lamden Docs: Installing Seneca Locally](https://docs.lamden.io/seneca/getting-started/installing-locally)
- Requires Redis
- Jupyter Notebook recomended IDE
- MACOSX: install unittest with homebrew
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

***
## Quantum Experimentation
***
### [Strawberry Fields Quantumn Library](https://strawberryfields.readthedocs.io/en/latest/introduction.html#introduction)
```
python 3.7.2
conda install tensorflow
python -m pip install strawberryfields
```
  



