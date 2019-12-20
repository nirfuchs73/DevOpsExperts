import Utils


# update the score file with the new score
def add_score(points):
    print('points', points)
    try:  # read current score from file
        file = open(Utils.SCORES_FILE_NAME, 'r', encoding='utf-8')
        current_score = file.read()
        # print('current_score', current_score)
        file.close()
    except:  # if file does not exist current_score = 0
        current_score = 0
    finally:  # write the new score to the file
        new_score = points + int(current_score)
        # print('new_score', new_score)
        file = open(Utils.SCORES_FILE_NAME, 'w', encoding='utf-8')
        file.write(str(new_score))
        file.close()
