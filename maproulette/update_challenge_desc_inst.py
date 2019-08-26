from maproulette import *
import json


def update_challenge_info(check_name):
    description = config_json[
        check_name][
        'challenge'][
        'description']
    instructions = config_json[
        check_name][
        'challenge'][
        'instruction']
    challenge['description'] = description
    challenge['instruction'] = instructions
    updated_data = json.dumps(challenge)

    return updated_data


if __name__ == '__main__':
    s = Server(api_key='3695|886c3315-18ed-40f3-ac3b-ebc7e52ad7b1',
               project_id=3891)
    mr_challenges = s.get(
        path="project/217/challenges?limit=2000&page=0",
        use_api_key=True)

    with open(
            '/Users/danielcastro/Documents/github/CheckFiles/checks.json'
    ) as config_file:
        config_json = json.load(config_file)
        for challenge in mr_challenges:
            if 'Invalid Lanes Tag' in challenge['name']:
                data = update_challenge_info('InvalidLanesTagCheck')
                s.put(path=f'challenge/{challenge["id"]}', payload=data)

            elif 'Invalid Turn Restriction' in challenge['name']:
                data = update_challenge_info('InvalidTurnRestrictionCheck')
                s.put(path=f'challenge/{challenge["id"]}', payload=data)

            elif 'Sharp Angle Road' in challenge['name']:
                data = update_challenge_info('SharpAngleCheck')
                s.put(path=f'challenge/{challenge["id"]}', payload=data)

            elif 'Floating Ways / Disconnected Road' in challenge['name']:
                data = update_challenge_info('FloatingEdgeCheck')
                s.put(path=f'challenge/{challenge["id"]}', payload=data)

            elif 'Connectivity Check' in challenge['name']:
                data = update_challenge_info('ConnectivityCheck')
                s.put(path=f'challenge/{challenge["id"]}', payload=data)

            elif 'Sink Islands & Impossible Routing' in challenge['name']:
                data = update_challenge_info('SinkIslandCheck')
                s.put(path=f'challenge/{challenge["id"]}', payload=data)

            elif 'Malformed Roundabout' in challenge['name']:
                data = update_challenge_info('MalformedRoundaboutCheck')
                s.put(path=f'challenge/{challenge["id"]}', payload=data)

            elif 'Crossing Roads' in challenge['name']:
                data = update_challenge_info('EdgeCrossingEdgeCheck')
                s.put(path=f'challenge/{challenge["id"]}', payload=data)

