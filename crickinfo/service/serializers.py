from rest_framework import serializers
from service.models import Match, Country, Player

class MathcGetSerializer(serializers.ModelSerializer):
	country1 = serializers.CharField(source="country1.name")
	country1 = serializers.CharField(source="country2.name")
	class Meta:
		model = Match
		fields=['country1','players',"country2"]
		
	def get_data(self):
		data = self.data
		for ind,row in enumerate(data):
			names=[]
			for player_id in row['players']:
				name = Player.objects.get(id=player_id).name
				names.append(name)
			data[ind]=names
		return data
	

class MatchSerializer(serializers.Serializer):
	#countries = serializers.ListField(require=False)
	countries = serializers.ListField()
	players = serializers.ListField()

	def validate_countries(self, value):
		for cnt in value:
			country = Country.objects.filter(name=cnt)
			if not country:
				#raise Exception()
				err = "country %s not found" % cnt
				raise serializers.ValidationError(err)
		return value
	def validate_players(self, value):
		for ply in value:
			plys = Player.objects.filter(name=ply)
			if not plys:
				err = "player %s not found" % ply
				raise serializers.ValidationError(err)
		return value

