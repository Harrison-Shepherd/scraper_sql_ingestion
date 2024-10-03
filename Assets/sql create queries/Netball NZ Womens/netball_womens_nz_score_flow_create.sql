CREATE TABLE netball_womens_nz_score_flow (
  period INT NOT NULL,
  distanceCode INT NOT NULL,
  scorepoints INT NOT NULL,
  periodSeconds INT NOT NULL,
  positionCode VARCHAR(45) NOT NULL,
  squadId INT NOT NULL,
  playerId INT NOT NULL,
  scoreName VARCHAR(45) NOT NULL,
  matchId INT NOT NULL,
  scoreFlowId INT NOT NULL,
  PRIMARY KEY (scoreFlowId)
);
