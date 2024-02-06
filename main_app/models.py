from django.db import models

RARITY_OPTIONS= [
    ('Common', 'Common'),
    ('Uncommon', 'Uncommon'),
    ('Rare', 'Rare'),
    ('Very Rare', 'Very Rare'),
    ('Extinct in the Wild', 'Extinct in the Wild'),
]

# Create your models here.
class RarePlant(models.Model):
    common_name = models.CharField(max_length=200, blank=True, default='')
    botanical_name = models.CharField(max_length=200, unique=True, default='')
   # image = models.ImageField(upload_to='plants/', blank=True)
    acquisition_date = models.DateField()
    rarity = models.TextField(help_text='"Common", "Uncommon", "Rare", "Very Rare", "Extinct in the Wild."', choices=RARITY_OPTIONS, default='')
    description = models.TextField(help_text="leaf shape, flower color, growth habit, and any distinctive features.", default='')
    sunlight = models.CharField(max_length=255, help_text="Sunlight requirements, e.g., full sun, partial shade, full shade.", default='')
    waterings = models.CharField(max_length=255, help_text="Watering frequency, e.g., twice a week, daily, every two weeks.", default='')
    temperature = models.CharField(max_length=255, help_text="Optimal temperature range, e.g., 65-75°F (18-24°C).", default='')
    humidity = models.CharField(max_length=255, help_text="Preferred humidity level, e.g., high, medium, low.", default='')
    soil_needs = models.CharField(max_length=255, help_text="Soil type and pH preference, e.g., well-draining, loamy soil with a pH of 6.0-7.0.", default='')
    myth_name = models.CharField(max_length=200, default='')
    description = models.TextField()
    origin_country = models.CharField(max_length=100, blank=True, default='')
    uses = models.TextField(blank=True, help_text="Describe traditional or contemporary uses of the plant related to the mythology, including medicinal, ornamental, or other utilitarian purposes.", default='')
    natural_history = models.TextField(blank=True, help_text="Provide information on the plant's natural history, including its discovery, historical range, and changes in its distribution or abundance over time.", default='')
    cultivation = models.TextField(blank=True, help_text="Outline cultivation methods tied to the plant’s historical or mythological significance, if any, including traditional practices or symbolic cultivation methods.", default='')
    notes = models.TextField(blank=True, null=True, default='')
    
    
    def __str__(self):
        return self.common_name
   

    

