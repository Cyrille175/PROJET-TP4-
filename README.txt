Voici le README de notre projet



pour dylan:

-> ajouter: from saveMouvement import save_movement, flush_movement
-> ajouter: save_movement("...") a chaqune des fonction _case()

def appui_fw1(self):
      forward_case()
      save_movement("forward_case")

      def appui_bw1(self):
      backward_case()
      save_movement("backward_case")

    def appui_r1(self):
      right_case()
      save_movement("right_case")

    def appui_l1(self):
      left_case()
      save_movement("left_case")
-> ajouter: la fonction flush dans _std:

def appui_std(self):
    stand()
    flush_movement()

