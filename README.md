# beCloudReady-Interview-2022


## Solutions

0. **Docker
Can be found inside [0.docker](https://github.com/sammdu/beCloudReady-Interview-2022/tree/main/0.docker).**
1. **Shell
Can be found inside [1.shell](https://github.com/sammdu/beCloudReady-Interview-2022/tree/main/1.shell).**
2. **Python
Can be found inside [2.python](https://github.com/sammdu/beCloudReady-Interview-2022/tree/main/2.python).**
  * 2.1. Setup and running   
  Ensure docker is set up correctly. Then: 
    * Build docker image by `./build.sh`
    * Run docker image by `./run.sh`   
    * Visit [http://localhost](http://localhost) to access the API endpoints.
    * **Endpoints**:
      * `GET /`: guest list of all guests
      * `GET /add?name=NewGuestName`: add a new guest by the name of `NewGuestName`
      * `GET /guest/<gid>?name=NewGuestName`: change guest `<gid>`'s name to `NewGuestName`
      * `DELETE /guest/<gid>`: delete guest `<gid>`

3. **Linux**
    Setup complete.
    SSHD config:
    ```
    Subsystem	sftp	internal-sftp -d /
    Match Group sftpusers
    ChrootDirectory /home/sftpusers
    
    # allow `user` to login with password
    Match User user
    PasswordAuthentication yes
    Match all
    ```
