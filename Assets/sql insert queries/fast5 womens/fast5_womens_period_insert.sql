INSERT INTO fast5_womens_period (
  rebounds, turnoverHeld, centrePassToGoalPerc, penalties, deflectionWithNoGain, generalPlayTurnovers, 
  interceptPassThrown, gain, points, goalMisses, blocked, deflectionWithGain, goalAssists, tossUpWin, centrePassReceives, 
  obstructionPenalties, feeds, playerId, goals, offsides, secondPhaseReceive, badPasses, period, breaks, blocks, badHands, 
  missedGoalTurnover, squadId, startingPositionCode, possessionChanges, goalAttempts, goalAttempts3, goalAttempts2, 
  contactPenalties, goalAttempts1, quartersPlayed, minutesPlayed, feedWithAttempt, unforcedTurnovers, pickups, goals1, 
  currentPositionCode, gainToGoalPerc, intercepts, goals3, goals2, matchId, periodId
) 
VALUES (
  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);
