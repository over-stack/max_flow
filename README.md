# 1736. Chinese Hockey

### Time limit: 2.0 second

### Memory limit: 64 MB

Sergey and Denis closely followed the Chinese Football Championship, which has just come to an end. They supported the Katraps and Komolotiv teams, but, unfortunately, these teams tied for last place in the championship. Sergey was so disappointed that he suggested Denis that they change to hockey fans.

There are n teams competing in the Chinese Ice Hockey Championship. During the season, each team must play with each other team exactly one game. If a team wins in the regulation time, it gets 3 points and the losing team gets 0 points. If the regulation time is ended in a draw, then the overtime is played. The team that wins in the overtime gets 2 points and the team that loses gets 1 point. A game can't end in a draw in ice hockey.
Denis wants to determine which team he will support. In order to make the choice, he has found a table on the Web in which it is shown for each team how many points it scored in the last year's season. Sergey suspects that there is a mistake in this table because no all-play-all tournament could end with such results. Is Sergey right?

### Input

The first line contains the integer n (2 ≤ n ≤ 200). The second line contains n space-separated non-negative integers; they are the scores of the teams in the previous championship. The scores are given in the non-increasing order. The sum of all the scores is 3n(n–1)/2. None of the teams scored more than 3(n–1) points.

### Output

If Sergey is right and there is a mistake in the table, output “INCORRECT” in the only line. Otherwise, in the first line output “CORRECT” and in the following n(n–1)/2 lines output the results of the games. Each result must have the form “i ? j”, where i and j are the numbers of the teams that played the game and ? can be <, <=, >=, or >, which means that the first team lost in the regulation time, lost in the overtime, won in the overtime, and won in the regulation time, respectively. The teams are numbered from 1 to n in the order in which they are given in the input.
