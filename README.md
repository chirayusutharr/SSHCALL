# SSH Terminal Chat

A simple terminal-based chat application built in Python to learn SSH, networking, multithreading, and file-based communication.

This project is designed as a learning exercise rather than a production-ready chat application. It explores how two users connected through SSH can communicate using a shared chat log, with the goal of gradually evolving into a socket-based real-time chat system.


---



* Python 3
* SSH (Secure Shell)
* Terminal Programming
* Multithreading (`threading`)
* File I/O
* Networking Fundamentals


---

## Requirements

* Python 3.10+
* SSH Server
* Linux/macOS (or Windows with OpenSSH Server)
* Two SSH terminals connected to the same machine

---

## Start an SSH Session

From another computer:

```bash
ssh username@server-ip
```


## Run the Chat

Navigate to the project directory:

```bash
cd SSH-Terminal-Chat


python3 chat.py
```

Open another SSH session and run the same command.

Both users can now exchange messages through the shared log.

---



---


development as part of a networking and systems programming learning journey.
