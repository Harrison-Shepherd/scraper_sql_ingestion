CREATE TABLE fast5_womens_score_flow (
  period INT NOT NULL,
  distanceCode INT DEFAULT NULL,
  scorePoints INT NOT NULL,
  periodSeconds INT NOT NULL,
  positionCode INT DEFAULT NULL,
  squadId INT NOT NULL,
  playerId INT NOT NULL,
  scoreName VARCHAR(50) NOT NULL,
  matchId INT NOT NULL,
  scoreFlowId VARCHAR(50) NOT NULL,
  PRIMARY KEY (scoreFlowId)
);
