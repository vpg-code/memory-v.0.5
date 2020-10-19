import arcade

import memoryhandler

ANCHO = 1200
ALTO = 900

SCREEN_TITLR = "MEMORY"


card_img_list = [
    "1", "2", "3", "4",
    "5", "6", "1", "2",
    "3", "4", "5", "6",
]


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(ANCHO, ALTO, SCREEN_TITLR)
        self.card_list = None
        self.card_change_list = None

    def setup(self):
        self.card_list = arcade.SpriteList()

        for i in range(card_img_list):

        for y in range(3):
            for x in range(4):
                card1 = arcade.Sprite("./Img/cardBack_red1.png", 1)
                card1.center_x = 0 + 80 + (x * 150)
                card1.center_y = ALTO - 100 - (y * 195)
                self.card_list.append(card1)

    def on_draw(self):
        arcade.start_render()
        self.card_list.draw()
        self.card_change_list.draw()

    def update(self, delta_time):
        self.card_list.update()

    def on_mouse_press(self, x, y, button, modifiers):
        click_list = arcade.get_sprites_at_point((x, y), self.card_list)

        for card in click_list:
            self.card_change_list = arcade.SpriteList()

            card1 = arcade.Sprite("./Img/card/card" +
                                  str(card_img_list[self.card_list.index(card)]) + ".png", 1)
            card1.center_x = card.center_x
            card1.center_y = card.center_y
            self.card_change_list.append(card1)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
