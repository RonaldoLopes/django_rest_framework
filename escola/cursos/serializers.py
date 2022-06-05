from rest_framework import serializers
from django.db.models import Avg
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {"email": {"write_only": True}}
        model = Avaliacao
        fields = (
            "id",
            "curso",
            "nome",
            "email",
            "comentario",
            "avaliacao",
            "criacao",
            "ativo",
        )


class CursoSerializer(serializers.ModelSerializer):
    # nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="avaliacao-detail"
    )
    media_avaliacoes = serializers.SerializerMethodField()
    # primary key related Field
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            "id",
            "titulo",
            "url",
            "criacao",
            "ativo",
            "avaliacoes",
            "media_avaliacoes",
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.all().aggregate(media=Avg("avaliacao"))["media"]
        if media is None:
            return 0
        return media
