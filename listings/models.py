from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


"""class setting(models.Model):
    class Theme(models.TextChoices):
        Classe centralisant les noms de thèmes et leur classe CSS correspondante
        OCEAN = "theme-ocean", "Ocean"
        DARK = "theme-dark", "Dark"
        MINT = "theme-mint", "Mint"
        SAND = "theme-sand", "Sand"
        GLACIER = "theme-glacier", "Glacier"
        FIRE = "theme-fire", "Fire"
        PINK = "theme-pink", "Pink"
        VIOLET = "theme-violet", "Violet"
        AMBER = "theme-amber", "Amber"
        CYAN = "theme-cyan", "Cyan"
        LIME = "theme-lime", "Lime"
        CORAL = "theme-coral", "Coral"
        TEAL = "theme-teal", "Teal"
        INDIGO = "theme-indigo", "Indigo"
        ROSE = "theme-rose", "Rose"

    # Exemple d'utilisation dans le modèle
    theme = models.CharField(max_length=20, choices=Theme.choices, default=Theme.OCEAN)
	  """
	    
class Band(models.Model):
    class Genre(models.TextChoices):
        # 🎸 Rock / Metal
        ALTERNATIVE_ROCK = 'AR', 'Alternative Rock'
        HARD_ROCK = 'HR', 'Hard Rock'
        CLASSIC_ROCK = 'CR', 'Classic Rock'
        METAL = 'MT', 'Metal'
        PUNK_ROCK = 'PR', 'Punk Rock'
        INDIE_ROCK = 'IR', 'Indie Rock'

        # 🎤 Pop / Électro
        POP = 'POP', 'Pop'
        SYNTH_POP = 'SP', 'Synth Pop'
        ELECTRONIC = 'EL', 'Electronic'
        HOUSE = 'HO', 'House'
        TECHNO = 'TC', 'Techno'
        EDM = 'EDM', 'EDM (Electronic Dance Music)'

        # 🎧 Hip-hop / R&B / Rap
        HIP_HOP = 'HH', 'Hip Hop'
        RAP = 'RAP', 'Rap'
        RNB = 'RNB', 'R&B / Soul'
        TRAP = 'TR', 'Trap'

        # 🎻 Jazz / Blues / Soul
        JAZZ = 'JZ', 'Jazz'
        BLUES = 'BL', 'Blues'
        SOUL = 'SO', 'Soul'
        FUNK = 'FK', 'Funk'

        # 🎶 Autres styles
        COUNTRY = 'CO', 'Country'
        REGGAE = 'RG', 'Reggae'
        LATIN = 'LA', 'Latin'
        FOLK = 'FO', 'Folk'
        GOSPEL = 'GP', 'Gospel'
        AFROBEAT = 'AF', 'Afrobeat'
        WORLD = 'WO', 'World Music'
        CLASSICAL = 'CL', 'Classical'
        K_POP = 'KP', 'K-Pop'

    # 🏷️ Champs du modèle Band
    name = models.CharField(max_length=100)
    genre = models.CharField(choices=Genre.choices, max_length=50)
    biography = models.CharField(max_length=1000)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2025)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    # like_new = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Listing(models.Model):
    class Type(models.TextChoices):
        # 💿 Musique et enregistrements
        RECORDS = 'RC', 'Records (Vinyles, CD, Cassettes)'
        DIGITAL_ALBUM = 'DA', 'Digital Album'
        SINGLE = 'SG', 'Single'
        LIVE_ALBUM = 'LA', 'Live Album'
        COMPILATION = 'CP', 'Compilation'

        # 👕 Vêtements et accessoires
        CLOTHING = 'CT', 'Clothing (T-Shirts, Hoodies, etc.)'
        HATS = 'HT', 'Hats / Caps'
        SHOES = 'SH', 'Shoes'
        ACCESSORIES = 'AC', 'Accessories (Bracelets, Chains, etc.)'
        BAGS = 'BG', 'Bags / Backpacks'

        # 🖼️ Articles visuels et décoratifs
        POSTERS = 'PT', 'Posters'
        STICKERS = 'ST', 'Stickers'
        ARTWORK = 'AW', 'Artwork / Paintings'
        PHOTOGRAPHY = 'PH', 'Photography Prints'

        # 📀 Instruments & matos
        INSTRUMENT = 'IN', 'Musical Instrument'
        EQUIPMENT = 'EQ', 'Studio / Audio Equipment'
        SHEET_MUSIC = 'SM', 'Sheet Music / Tabs'

        # 🎁 Produits spéciaux ou autres
        LIMITED_EDITION = 'LE', 'Limited Edition Item'
        COLLECTIBLES = 'CL', 'Collectible Item'
        GIFT = 'GF', 'Gift Item / Merch Box'
        TICKETS = 'TK', 'Concert Tickets'
        MISC = 'MS', 'Miscellaneous'

    # 🏷️ Champs du modèle Listing
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2025)],
        null=True, blank=True
    )
    type = models.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, blank=True, on_delete=models.SET_NULL, related_name="listings")
    def __str__(self):
        return self.title
        
        
    #python manage.py loaddata data.json