INSERT INTO fast5_mens_match (
  rebounds, turnoverHeld, centrePassToGoalPerc, penalties, deflectionWithNoGain, 
  generalPlayTurnovers, interceptPassThrown, gain, points, goalMisses, blocked, deflectionWithGain, 
  goalAssists, tossUpWin, centrePassRecieves, obstructionPenalties, feeds, playerId, goals, offsides, 
  secondPhaseReceive, badPasses, breaks, blocks, badHands, missedGoalTurnover, squadId, 
  deflectionPossessionGain, possessionChanges, startingPositionCode, goalAttempts, goalAttempts3, goalAttempts2, 
  contactPenalties, goalAttempts1, quartersPlayed, minutesPlayed, feedWithAttempt, unforcedTurnovers, pickups, 
  goals1, currentPositionCode, gainToGoalPerc, intercepts, goals3, goals2, shortDisplayName, firstName, surname, 
  displayName, squadName, homeId, awayId, opponent, round, fixtureId, sportId, matchId
) 
VALUES (
  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);
