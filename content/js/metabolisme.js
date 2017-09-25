angular.module('metabolisme', [])
  .controller('Controller', function() {
    var self = this;

    var distance = 0;
    var heures = minutes = 0;
    var denivele = 0;
    var nom = "";

    var sortie_chevreuse = {
      distance: 87,
      heures: 4,
      minutes: 50,
      denivele: 700,
      nom: "Chevreuse"
    }

    var sortie_longchamp = {
      distance: 42,
      heures: 1,
      minutes: 32,
      denivele: 128,
      nom: "Longchamp"
    }

    self.set = function(sortie) {
      self.distance = sortie.distance;
      self.heures = sortie.heures;
      self.minutes = sortie.minutes;
      self.denivele = sortie.denivele;
      self.nom = sortie.nom;
    }

    self.chevreuse = function() {
      self.set(self.sortie_chevreuse);
    }
    self.longchamp = function() {
      self.set(self.sortie_longchamp);
    }

    self.chevreuse();

  });
