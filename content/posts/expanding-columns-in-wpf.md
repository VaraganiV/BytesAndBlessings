---
title: "Expanding Columns in WPF"
description: "How to dynamically expand DataGrid column height in WPF to handle multi-line cell content using RowDetails and custom templates."
date: 2012-01-30
draft: false
categories:
  - tech
ShowToc: true
TocOpen: false
tags:
  - wpf
  - dotnet
  - ui
cover:
  image: "images/covers/expanding-columns-in-wpf-cover.svg"
  alt: "Cover image"
  relative: false
---

WPF  
Expanding the column height at Run
Time

## The Problem

We were supposed to handle a case
where the one of the columns in the data grid can contain multiple lines of
data, and it should be only allowed when the use enters that particular cell.

In a sense, were supposed to
expand the height of a data grid column at run time when the cell is IN edit
mode and collapse and show the multiline text as tooltip when the cell is NOT
in edit mode.

</a>
</figure>

## The Solution

How did we achieve this

We achieved this functionality
by manipulation the styles of data grid. We defined two different styles
for the specified column, one the Element Style and other is
the EditingElementStyle.

|  |
| --- |
| <dg:DataGridTextColumn         Cell  Header  Elementfont-family: Verdana, sans-serif; font-size: 8pt; text-align: left; text-indent: 48px;">TextColCommentEleStyle}"  EditingElementfont-family: Verdana, sans-serif; font-size: 8pt; text-align: left; text-indent: 0.5in;">TextColCommentEleEditStyle}"  .  .  .    <Style x:Key=" **TextColCommentEleStyle** " TargetType="{x:Type TextBlock}">  <Setter Property="ToolTip" Value="{Binding Path=Comments}" />  <Setter Property="TextWrapping" Value="NoWrap" />  <Setter Property="TextAlignment" Value="Left" />  <Setter Property="HorizontalAlignment" Value="Stretch" />  <Setter Property="VerticalAlignment" Value="Top" />  <Setter Property="Height" Value="18"/>  <Setter Property="Padding" Value="3" />  </Style>  <Style x:Key=" **TextColCommentEleEditStyle** " TargetType="{x:Type TextBox}">  <Setter Property="Height" Value="60"/>  <Setter Property="TextWrapping" Value="NoWrap" />  <Setter Property="AcceptsReturn" Value="true" />  <Setter Property="VerticalAlignment" Value="Top"/>  </Style> |