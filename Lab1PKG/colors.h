
#ifndef COLORS_H
#define COLORS_H

#include <QMainWindow>
#include <QColorDialog>
#include <QWidget>
#include <QPainter>
#include <QColor>
#include <QSlider>
#include <QtMath>
#include <QtAlgorithms>


QT_BEGIN_NAMESPACE
namespace Ui { class Colors; }
QT_END_NAMESPACE

class Colors : public QMainWindow

{
    Q_OBJECT

public:
    Colors(QWidget *parent = nullptr);
    void RGBToLAB();
    void LABToRGB();
    ~Colors();

private:
    Ui::Colors *ui;
    QColorDialog* cDialog;
    QColor currentColor;
    float red;
    float green;
    float blue;
    float cyan;
    float yellow;
    float magenta;
    float key;
    float lightness;
    float a;
    float bl;


public slots:
    void rangeClicked();
    void colorDialogSelected();
    void colorChanged();
    void slotRGBSliderMoved();
    void slotCMYKSliderMoved();
    void slotLABSliderMoved();
};

#endif // COLORS_H
