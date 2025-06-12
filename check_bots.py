import os
import argparse
import protobuf.bot_pb2

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--average_power_limit', type=float)
parser.add_argument('-s', '--average_speed_limit', type=float)
args = parser.parse_args()

path = os.path.join('storage', 'bots', 'ghosts')
for (root, dirs, files) in os.walk(path):
    for file in files:
        if file.endswith('.bin'):
            full_path = os.path.join(root, file)
            bot = protobuf.bot_pb2.Bot()
            with open(full_path, 'rb') as f:
                bot.ParseFromString(f.read())
            if len(bot.states) < 200:
                print('Removing %s (too short)' % full_path)
                os.remove(full_path)
                continue
            last = 0
            gaps = 0
            for state in bot.states:
                if state.time - last > 4:
                    gaps += 1
                last = state.time
            if gaps > 1:
                print('Removing %s (%s gaps)' % (full_path, gaps))
                os.remove(full_path)
            if args.average_power_limit:
                avg_power = sum([s.power for s in bot.states]) / len(bot.states)
                if avg_power > args.average_power_limit:
                    print('Removing %s (power = %.2f)' % (full_path, avg_power))
                    os.remove(full_path)
            if args.average_speed_limit:
                avg_speed = sum([s.speed for s in bot.states]) / len(bot.states) / 1000000
                if avg_speed > args.average_speed_limit:
                    print('Removing %s (speed = %.2f)' % (full_path, avg_speed))
                    os.remove(full_path)
print('Done.')
input()
