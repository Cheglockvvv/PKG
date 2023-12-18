
#include "colors.h"
#include "ui_colors.h"


Colors::Colors(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Colors)
{
    red = 0;
    green = 0;
    blue = 0;
    lightness = 0;
    a = 0;
    bl = 0;
    currentColor = QColor(red, green, blue);
    //colorChanged();
    this->setFixedSize(1300,700);
    ui->setupUi(this);
    cDialog = new QColorDialog;
    ui->label->setText("Red");
    ui->label_2->setText("Green");
    ui->label_3->setText("Blue");

    ui->horizontalSlider->setRange(0, 255);
    ui->horizontalSlider_2->setRange(0, 255);
    ui->horizontalSlider_3->setRange(0, 255);
    ui->horizontalSlider_4->setRange(0, 100);
    ui->horizontalSlider_5->setRange(-128, 127);
    ui->horizontalSlider_6->setRange(-128, 127);
    ui->horizontalSlider_7->setRange(0, 255);
    ui->horizontalSlider_8->setRange(0, 255);
    ui->horizontalSlider_9->setRange(0, 255);
    ui->horizontalSlider_10->setRange(0, 255);


    ui->label_15->setStyleSheet("QLabel{background-color:rgb(" + QString::number(red) + "," + QString::number(green) + "," + QString::number(blue) + ")}");
    QObject::connect(ui->pushButton,SIGNAL(clicked()),SLOT(rangeClicked()));
    QObject::connect(cDialog, SIGNAL(colorSelected(QColor)), SLOT(colorDialogSelected()));
    QObject::connect(ui->horizontalSlider, SIGNAL(sliderReleased()), SLOT(slotRGBSliderMoved()));
    QObject::connect(ui->horizontalSlider_2, SIGNAL(sliderReleased()), SLOT(slotRGBSliderMoved()));
    QObject::connect(ui->horizontalSlider_3, SIGNAL(sliderReleased()), SLOT(slotRGBSliderMoved()));
    QObject::connect(ui->horizontalSlider_4, SIGNAL(sliderReleased()), SLOT(slotLABSliderMoved()));
    QObject::connect(ui->horizontalSlider_5, SIGNAL(sliderReleased()), SLOT(slotLABSliderMoved()));
    QObject::connect(ui->horizontalSlider_6, SIGNAL(sliderReleased()), SLOT(slotLABSliderMoved()));
    QObject::connect(ui->horizontalSlider_7, SIGNAL(sliderReleased()), SLOT(slotCMYKSliderMoved()));
    QObject::connect(ui->horizontalSlider_8, SIGNAL(sliderReleased()), SLOT(slotCMYKSliderMoved()));
    QObject::connect(ui->horizontalSlider_9, SIGNAL(sliderReleased()), SLOT(slotCMYKSliderMoved()));
    QObject::connect(ui->horizontalSlider_10, SIGNAL(sliderReleased()), SLOT(slotCMYKSliderMoved()));
    QObject::disconnect(SIGNAL(valueChanged(int)), ui->horizontalSlider, SLOT(setSliderPosition));
    QObject::disconnect(SIGNAL(valueChanged(int)), ui->horizontalSlider_2, SLOT(setSliderPosition()));
    QObject::disconnect(SIGNAL(valueChanged(int)), ui->horizontalSlider_3, SLOT(setSliderPosition()));
    QObject::disconnect(SIGNAL(valueChanged(int)), ui->horizontalSlider_4, SLOT(setSliderPosition()));
    QObject::disconnect(SIGNAL(valueChanged(int)), ui->horizontalSlider_5, SLOT(setSliderPosition()));
    QObject::disconnect(SIGNAL(valueChanged(int)), ui->horizontalSlider_6, SLOT(setSliderPosition()));
    QObject::disconnect(SIGNAL(valueChanged(int)), ui->horizontalSlider_7, SLOT(setSliderPosition()));
    QObject::disconnect(SIGNAL(valueChanged(int)), ui->horizontalSlider_8, SLOT(setSliderPosition()));
    QObject::disconnect(SIGNAL(valueChanged(int)), ui->horizontalSlider_9, SLOT(setSliderPosition()));
    QObject::disconnect(SIGNAL(valueChanged(int)), ui->horizontalSlider_10, SLOT(setSliderPosition()));
}

void Colors::colorDialogSelected()
{
    currentColor = cDialog->selectedColor();
    ui->label_15->setStyleSheet("QLabel{background-color:rgb(" + QString::number(currentColor.red()) + "," + QString::number(currentColor.green()) + "," + QString::number(currentColor.blue()) + ")}");
    red = currentColor.red();
    green = currentColor.green();
    blue = currentColor.blue();
    RGBToLAB();
    colorChanged();
}

void Colors::rangeClicked()
{
    cDialog->open();
}

// changing of color triggers movement of slider and changes the value int the lineEdit, everything is simple
void Colors::colorChanged()
{
    ui->horizontalSlider->setSliderPosition(red);
    ui->lineEdit->setText(QString::number(red));

    ui->horizontalSlider_2->setSliderPosition(green);
    ui->lineEdit_2->setText(QString::number(green));

    ui->horizontalSlider_3->setSliderPosition(blue);
    ui->lineEdit_3->setText(QString::number(blue));

    ui->horizontalSlider_4->setSliderPosition(lightness);
    ui->lineEdit_4->setText(QString::number(lightness));

    ui->horizontalSlider_5->setSliderPosition(a);
    ui->lineEdit_5->setText(QString::number(a));

    ui->horizontalSlider_6->setSliderPosition(bl);
    ui->lineEdit_6->setText(QString::number(bl));

    ui->horizontalSlider_7->setSliderPosition(currentColor.cyan());
    ui->lineEdit_7->setText(QString::number(currentColor.cyan()));

    ui->horizontalSlider_8->setSliderPosition(currentColor.magenta());
    ui->lineEdit_8->setText(QString::number(currentColor.magenta()));

    ui->horizontalSlider_9->setSliderPosition(currentColor.yellow());
    ui->lineEdit_9->setText(QString::number(currentColor.yellow()));

    ui->horizontalSlider_10->setSliderPosition(currentColor.black());
    ui->lineEdit_10->setText(QString::number(currentColor.black()));


}

void Colors::slotRGBSliderMoved()
{
    red = ui->horizontalSlider->value();
    green = ui->horizontalSlider_2->value();
    blue = ui->horizontalSlider_3->value();

    float r = red / 255;
    float g = green / 255;
    float b = blue / 255;

    QVector <float> rgbs;
    rgbs.push_back(1 - r);
    rgbs.push_back(1 - g);
    rgbs.push_back(1 - b);
    std::sort(std::begin(rgbs), std::end(rgbs));
    key = rgbs[0];

    cyan = (1 - r - key) / (1 - key) * 255;
    magenta = (1 - g - key) / (1 - key) * 255;
    yellow = (1 - b - key) / (1 - key) * 255;

    currentColor = QColor(red, green, blue);
    ui->label_15->setStyleSheet("QLabel{background-color:rgb(" + QString::number(red) + "," + QString::number(green) + "," + QString::number(blue) + ")}");

    RGBToLAB();
    colorChanged();

}

void Colors::slotCMYKSliderMoved()
{
    cyan = ui->horizontalSlider_7->value();
    magenta = ui->horizontalSlider_8->value();
    yellow = ui->horizontalSlider_9->value();
    key = ui->horizontalSlider_10->value();
    currentColor.setCmyk(cyan, magenta, yellow, key);
    int r = 255 * (1 - (cyan/255)) * (1 - (key/255));
    int g = 255 * (1 - (magenta/255)) * (1 - (key/255));
    int b = 255 * (1 - (yellow/255)) * (1 - (key/255));

    red = r;
    green = g;
    blue = b;

    RGBToLAB();

    ui->label_15->setStyleSheet("QLabel{background-color:rgb(" + QString::number(r) + "," + QString::number(g) + "," + QString::number(b) + ")}");
    colorChanged();
}

void Colors::slotLABSliderMoved()
{
    lightness = ui->horizontalSlider_4->value();
    a = ui->horizontalSlider_5->value();
    bl = ui->horizontalSlider_6->value();

    LABToRGB();

    currentColor = QColor(red, green, blue);
    ui->label_15->setStyleSheet("QLabel{background-color:rgb(" + QString::number(red) + "," + QString::number(green) + "," + QString::number(blue) + ")}");
    colorChanged();
}

void Colors::RGBToLAB()
{
    float r = red/255;
    float g = green/255;
    float b = blue/255;

    if (r > 0.04045)
    {
        r = qPow(((r + 0.055) / 1.055), 2.4);
    }
    else
    {
        r /= 12.92;
    }

    if (b > 0.04045)
    {
        b = qPow(((b + 0.055) / 1.055), 2.4);
    }
    else
    {
        b /= 12.92;
    }

    if (g > 0.04045)
    {
        g = qPow(((g + 0.055) / 1.055), 2.4);
    }
    else
    {
        g /= 12.92;
    }

    r *= 100;
    g *= 100;
    b *= 100;

    float x = r * 0.4124 + g * 0.3576 + b * 0.1805;
    float y = r * 0.2126 + g * 0.7152 + b * 0.0722;
    float z = r * 0.0193 + g * 0.1192 + b * 0.9505;

    x /= 95.047;
    y /= 100;
    z /= 108.883;

    if (x > 0.008856)
    {
        x = qPow(x, 0.3333);
    }
    else
    {
        x = (7.787 * x) + (16 / 116);
    }

    if (y > 0.008856)
    {
        y = qPow(y, 0.3333);
    }
    else
    {
        y = (7.787 * y) + (16 / 116);
    }

    if (z > 0.008856)
    {
        z = qPow(z, 0.3333);
    }
    else
    {
        z = (7.787 * z) + (16 / 116);
    }

    lightness = (116 * y) - 16;
    a = 500 * (x - y);
    bl = 200 * (y - z);
}

void Colors::LABToRGB()
{
    float y = (lightness + 16) / 116;
    float x = (a / 500) + y;
    float z = y - (bl / 200);

    if (qPow(y, 3) > 0.008856)
    {
        y = qPow(y, 3);
    }
    else
    {
        y = (y - 16/116) / 7.787;
    }

    if (qPow(x, 3) > 0.008856)
    {
        x = qPow(x, 3);
    }
    else
    {
        x = (x - 16/116) / 7.787;
    }

    if (qPow(z, 3) > 0.008856)
    {
        z = qPow(z, 3);
    }
    else
    {
        z = (z - 16/116) / 7.787;
    }

    x *= 95.047;
    y *= 100;
    z *= 108.883;

    x /= 100;
    y /= 100;
    z /= 100;

    float r = x *  3.2406 + y * -1.5372 + z * -0.4986;
    float g = x * -0.9689 + y *  1.8758 + z *  0.0415;
    float b = x *  0.0557 + y * -0.2040 + z *  1.0570;

    if (r < 0)
        r = 0;
    if (b < 0)
        b = 0;
    if (g < 0)
        g = 0;

    if (r > 0.0031308)
    {
        r = 1.055 * (qPow(r, 0.41666667)) - 0.055;
    }
    else
    {
        r *= 12.92;
    }

    if (g > 0.0031308)
    {
        g = 1.055 * (qPow(g, 0.41666667)) - 0.055;
    }
    else
    {
        g *= 12.92;
    }

    if (b > 0.0031308)
    {
        b = 1.055 * (qPow(b, 0.41666667)) - 0.055;
    }
    else
    {
        b *= 12.92;
    }

    red = r * 255;
    green = g * 255;
    blue = b * 255;

    if (red > 255)
        red = 255;
    if (green > 255)
        green = 255;
    if (blue > 255)
        blue = 255;
}

Colors::~Colors()
{
    delete ui;
}


