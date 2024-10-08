CREATE TABLE netball_womens_nz_match (
    rebounds INT,
    turnoverHeld INT,
    centrePassToGoalPerc INT,
    penalties INT,
    deflectionWithNoGain INT,
    generalPlayTurnovers INT,
    interceptPassThrown INT,
    gain INT,
    points INT,
    goalMisses INT,
    blocked INT,
    deflectionWithGain INT,
    goalAssists INT,
    tossUpWin INT,
    centrePassReceives INT,
    obstructionPenalties INT,
    feeds INT,
    playerId INT NOT NULL,
    goals INT,
    offsides INT,
    secondPhaseReceive INT,
    badPasses INT,
    breaks INT,
    blocks INT,
    badHands INT,
    missedGoalTurnover INT,
    squadId INT NOT NULL,
    deflectionPossessionGain INT,
    possessionChanges INT,
    startingPositionCode VARCHAR(45) NOT NULL,
    goalAttempts INT,
    contactPenalties INT,
    quartersPlayed INT,
    minutesPlayed INT,
    feedWithAttempt INT,
    unforcedTurnovers INT,
    pickups INT,
    currentPositionCode VARCHAR(45) NOT NULL,
    gainToGoalPerc INT,
    intercepts INT,
    shortDisplayName VARCHAR(45) NOT NULL,
    firstname VARCHAR(45) NOT NULL,
    surname VARCHAR(45) NOT NULL,
    displayName VARCHAR(45) NOT NULL,
    squadName VARCHAR(45) NOT NULL,
    homeId INT NOT NULL,
    awayId INT NOT NULL,
    opponent VARCHAR(45) NOT NULL,
    round INT NOT NULL,
    fixtureId INT NOT NULL,
    sportId INT NOT NULL,
    matchId INT NOT NULL,
    PRIMARY KEY (matchId)
);
