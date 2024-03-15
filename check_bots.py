import os
import protobuf.bot_pb2

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
print('Done.')
input()
