from django.db import models

from datetime import date

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
    rarity = models.CharField(choices=RARITY_OPTIONS, default='')
    description = models.TextField(help_text="leaf shape, flower color, growth habit, and any distinctive features.", default='')
    poisonous = models.BooleanField(default=False, blank=True, null=True)
    toxic = models.BooleanField(default=False, blank=True, null=True)
    
    def nurtured_for_today(self):
        today = date.today()
        return self.nurtures.filter(date=today).exists()
    
    def __str__(self):
        return self.common_name
   

    
class PlantCultivation(models.Model):
    sunlight = models.CharField(max_length=255, help_text="Sunlight requirements, e.g., full sun, partial shade, full shade.", default='')
    waterings = models.CharField(max_length=255, help_text="Watering frequency, e.g., twice a week, daily, every two weeks.", default='')
    temperature = models.CharField(max_length=255, help_text="Optimal temperature range, e.g., 65-75°F (18-24°C) option + shift + 8 for degree symbol.", default='')
    humidity = models.CharField(max_length=255, help_text="Preferred humidity level, e.g., high, medium, low.", default='')
    soil_needs = models.CharField(max_length=255, help_text="Soil type and pH preference, e.g., well-draining, loamy soil with a pH of 6.0-7.0.", default='')
    fertilizer_needs = models.CharField(max_length=255, default='')
    
    RarePlant = models.OneToOneField(RarePlant, on_delete=models.CASCADE)

    def __str__(self):
          return f"{self.RarePlant.common_name}"


class PlantOrigin(models.Model):
    origin_country = models.CharField(max_length=100, blank=True, default='')
    uses = models.TextField(blank=True, help_text="Describe traditional or contemporary uses of the plant related to the mythology, including medicinal, ornamental, or other utilitarian purposes.", default='')
    natural_history = models.TextField(blank=True, help_text="Provide information on the plant's natural history, including its discovery, historical range, and changes in its distribution or abundance over time.", default='')
    cultivation = models.TextField(blank=True, help_text="Outline cultivation methods tied to the plant’s historical or mythological significance, if any, including traditional practices or symbolic cultivation methods.", default='')
    myth_name = models.CharField(max_length=200, blank=True, null=True, default='')
    notes = models.TextField(blank=True, null=True, default='')
    
    RarePlant = models.OneToOneField(RarePlant, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.RarePlant.common_name} Origin - {self.origin_country}"
   
class PlantNurture(models.Model):
    RarePlant = models.ForeignKey('RarePlant', on_delete=models.CASCADE, related_name='nurtures')
    date = models.DateField()
    cleaned = models.BooleanField(default=False)
    met_required_light = models.BooleanField(default=False)
    met_required_humidity = models.BooleanField(default=False)
    soil_moisture = models.CharField(max_length=255, blank=True, null=True)
    soil_ph = models.DecimalField(max_digits=4, decimal_places=2)
    watered = models.BooleanField(default=False, blank=True, null=True)
    music_played = models.CharField(max_length=255, blank=True, null=True)
    overall_appearance = models.TextField()

    def __str__(self):
        return f"{self.RarePlant.common_name} was nurtured on {self.date}"
    
    class Meta:
        ordering = ['-date']
        
class MusicPlaylist(models.Model):
  name = models.CharField(max_length=50)
  Genre = models.CharField(max_length=20)
  length = models.DurationField()

  def __str__(self):
    return self.name