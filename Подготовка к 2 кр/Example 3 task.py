class History:
    def __init__(self, *feats, hero='Nobody'):
        self.feats = list(feats)
        self.hero = hero

    def __add__(self, other):
        combined_feats = sorted(list(set(self.feats + other.feats)))
        combined_hero = min(self.hero, other.hero)
        return History(*combined_feats, hero=combined_hero)

    def __iadd__(self, other):
        self.feats = self.feats + [feat for feat in other.feats if feat not in self.feats]
        return self

    def __call__(self, num):
        return sum([len(feat) for feat in self.feats if len(feat) % num != 0])

    def __str__(self):
        return 'History(hero:' + ' ' + self.hero + ', ' + 'feats:' + ' ' + ', '.join(self.feats) + ')'


if __name__ == '__main__':
    wow1 = ['discovery', 'perpetual motion machine', 'improbability', 'ion sword']
    wow2 = ['time machine', 'transformer', 'improbability', 'flying saucer', 'ion sword']
    h1 = History(*wow1, hero='Doctor Who')
    h2 = History(*wow2)
    h = h1 + h2
    print(h1, h2, h, sep='\n')


# предполагаемый вывод:
# History(hero: Doctor Who, feats: discovery, perpetual motion machine, improbability, ion sword)
# History(hero: Nobody, feats: time machine, transformer, improbability, flying saucer, ion sword)
# History(hero: Doctor Who, feats: discovery, flying saucer, improbability, ion sword, perpetual motion machine, time machine, transformer)

