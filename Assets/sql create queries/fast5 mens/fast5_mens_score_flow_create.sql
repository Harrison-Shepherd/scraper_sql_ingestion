CREATE TABLE fast5_mens_score_flow (
  period INT NOT NULL,
  distanceCode INT NOT NULL,
  scorePoints INT NOT NULL,
  periodSeconds INT NOT NULL,
  positionCode INT NOT NULL,
  squadId INT NOT NULL,
  playerId INT NOT NULL,
  scoreName VARCHAR(20) NOT NULL,
  matchId INT NOT NULL,
  scoreFlowId INT NOT NULL,
  PRIMARY KEY (scoreFlowId)
);
