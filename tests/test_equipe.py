def test_equipe_un_nom_promo(db):
    equipe = Equipe.objects.create(nom="Equipe A", promo="L1")
    assert equipe.nom
    assert equipe.promo 