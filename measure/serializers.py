# measure/serializers.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from .models import ContestMeasure
from rest_framework import serializers


class ContestMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestMeasure
        fields = ('we_vote_id', 'maplight_id', 'measure_title', 'measure_subtitle', 'measure_text', 'measure_url',
                  'google_civic_election_id', 'ocd_division_id',
                  'primary_party', 'district_name', 'district_scope', 'district_id', 'state_code',
                  'wikipedia_page_id', 'wikipedia_page_title', 'wikipedia_photo_url',
                  'ballotpedia_page_title', 'ballotpedia_photo_url',
                  )
