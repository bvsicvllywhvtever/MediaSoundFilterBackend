CREATE DATABASE IF NOT EXISTS mediasoundfilter;
USE mediasoundfilter;

CREATE TABLE IF NOT EXISTS Sound_Categories (
    id int NOT NULL AUTO_INCREMENT,
    category varchar(255) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS Sounds (
    id int NOT NULL AUTO_INCREMENT,
    sound varchar(255) NOT NULL,
    category int NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (category) REFERENCES Sound_Categories(id)
);

CREATE TABLE IF NOT EXISTS Sound_Times (
    id int NOT NULL AUTO_INCREMENT,
    video_id varchar(255) NOT NULL,
    sound int NOT NULL,
    start_time int NOT NULL,
    end_time int NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(sound) REFERENCES Sounds(id)
);

INSERT INTO Sound_Categories (category) VALUES ('Speech/Mouth');
INSERT INTO Sound_Categories (category) VALUES ('Other Human Noises');
INSERT INTO Sound_Categories (category) VALUES ('Human Movement');
INSERT INTO Sound_Categories (category) VALUES ('Environmental Movement');
INSERT INTO Sound_Categories (category) VALUES ('Phone/Alarms');

INSERT INTO Sounds (sound, category) VALUES ('Babbling', 1);
INSERT INTO Sounds (sound, category) VALUES ('Shouting', 1);
INSERT INTO Sounds (sound, category) VALUES ('Whispering', 1);
INSERT INTO Sounds (sound, category) VALUES ('Crying', 1);
INSERT INTO Sounds (sound, category) VALUES ('Baby Crying', 1);
INSERT INTO Sounds (sound, category) VALUES ('Whimpering', 1);
INSERT INTO Sounds (sound, category) VALUES ('Sighing', 1);
INSERT INTO Sounds (sound, category) VALUES ('Singing', 1);
INSERT INTO Sounds (sound, category) VALUES ('Humming', 1);
INSERT INTO Sounds (sound, category) VALUES ('Groaning', 1);
INSERT INTO Sounds (sound, category) VALUES ('Grunting', 1);
INSERT INTO Sounds (sound, category) VALUES ('Whistling', 1);
INSERT INTO Sounds (sound, category) VALUES ('Breathing', 1);
INSERT INTO Sounds (sound, category) VALUES ('Wheezing', 1);
INSERT INTO Sounds (sound, category) VALUES ('Snoring', 1);
INSERT INTO Sounds (sound, category) VALUES ('Gasping', 1);
INSERT INTO Sounds (sound, category) VALUES ('Panting', 1);
INSERT INTO Sounds (sound, category) VALUES ('Coughing', 1);
INSERT INTO Sounds (sound, category) VALUES ('Throat Clearing', 1);
INSERT INTO Sounds (sound, category) VALUES ('Eating', 1);
INSERT INTO Sounds (sound, category) VALUES ('Gargling', 1);
INSERT INTO Sounds (sound, category) VALUES ('Burping', 1);
INSERT INTO Sounds (sound, category) VALUES ('Hiccuping', 1);

INSERT INTO Sounds (sound, category) VALUES ('Sneezing', 2);
INSERT INTO Sounds (sound, category) VALUES ('Sniffing', 2);
INSERT INTO Sounds (sound, category) VALUES ('Farting', 2);

INSERT INTO Sounds (sound, category) VALUES ('Footsteps', 3);
INSERT INTO Sounds (sound, category) VALUES ('Finger Snapping', 3);
INSERT INTO Sounds (sound, category) VALUES ('Clapping', 3);

INSERT INTO Sounds (sound, category) VALUES ('Knocking', 4);
INSERT INTO Sounds (sound, category) VALUES ('Slamming', 4);
INSERT INTO Sounds (sound, category) VALUES ('Tapping', 4);
INSERT INTO Sounds (sound, category) VALUES ('Squeaking', 4);
INSERT INTO Sounds (sound, category) VALUES ('Drawer/Cupboard', 4);
INSERT INTO Sounds (sound, category) VALUES ('Pots and Pans', 4);
INSERT INTO Sounds (sound, category) VALUES ('Silverware', 4);
INSERT INTO Sounds (sound, category) VALUES ('Vacuum Cleaner', 4);
INSERT INTO Sounds (sound, category) VALUES ('Typing', 4);
INSERT INTO Sounds (sound, category) VALUES ('Clock', 4);
INSERT INTO Sounds (sound, category) VALUES ('Filing', 4);
INSERT INTO Sounds (sound, category) VALUES ('Clink', 4);
INSERT INTO Sounds (sound, category) VALUES ('Squish', 4);
INSERT INTO Sounds (sound, category) VALUES ('Clicking', 4);
INSERT INTO Sounds (sound, category) VALUES ('TV', 4);

INSERT INTO Sounds (sound, category) VALUES ('Siren', 5);
INSERT INTO Sounds (sound, category) VALUES ('Phone Ringing', 5);
INSERT INTO Sounds (sound, category) VALUES ('Phone Dialing', 5);
INSERT INTO Sounds (sound, category) VALUES ('Dial Tone', 5);
INSERT INTO Sounds (sound, category) VALUES ('Alarm Clock', 5);
INSERT INTO Sounds (sound, category) VALUES ('Buzzer', 5);
INSERT INTO Sounds (sound, category) VALUES ('Foghorn', 5);
INSERT INTO Sounds (sound, category) VALUES ('Whistle', 5);
INSERT INTO Sounds (sound, category) VALUES ('Beep', 5);
INSERT INTO Sounds (sound, category) VALUES ('Ding', 5);