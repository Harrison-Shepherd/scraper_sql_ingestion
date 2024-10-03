CREATE TABLE NRL_mens_score_flow (
  scoreFlowId INT NOT NULL,
  period INT NOT NULL,
  scorepoints INT NOT NULL,
  periodSeconds INT NOT NULL,
  squadId INT NOT NULL,
  playerId INT NOT NULL,
  scoreName VARCHAR(45) NOT NULL,
  matchId INT NOT NULL,
  PRIMARY KEY (scoreFlowId)
);
