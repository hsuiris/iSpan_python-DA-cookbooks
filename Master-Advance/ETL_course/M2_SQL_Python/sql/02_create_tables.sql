-- 學生資料表
CREATE TABLE IF NOT EXISTS students (
    sId       TEXT PRIMARY KEY,
    sName     TEXT NOT NULL,
    sGender   TEXT NOT NULL,
    sNickname TEXT NOT NULL
);

-- 老師資料表
CREATE TABLE IF NOT EXISTS teachers (
    tId   TEXT PRIMARY KEY,
    tName TEXT NOT NULL
);

-- 課程資料表
CREATE TABLE IF NOT EXISTS courses (
    cId          TEXT NOT NULL,
    cName        TEXT NOT NULL,
    credit       INTEGER NOT NULL,
    isCompulsory INTEGER NOT NULL,
    tId          TEXT NOT NULL,
    PRIMARY KEY (cId, tId),
    FOREIGN KEY (tId) REFERENCES teachers(tId)
);

-- 成績資料表
CREATE TABLE IF NOT EXISTS scores (
    sId   TEXT NOT NULL,
    cId   TEXT NOT NULL,
    score INTEGER NOT NULL,
    PRIMARY KEY (sId, cId),
    FOREIGN KEY (sId) REFERENCES students(sId),
    FOREIGN KEY (cId) REFERENCES courses(cId)
);
