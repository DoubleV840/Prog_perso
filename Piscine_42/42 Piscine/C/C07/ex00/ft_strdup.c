/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: wberger <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/19 11:47:02 by wberger           #+#    #+#             */
/*   Updated: 2022/07/20 18:51:12 by wberger          ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */
#include	<stdlib.h>

char	*ft_strdup(char *src)
{
	int		i;
	int		j;
	char	*tab;

	i = 0;
	j = 0;
	while (src[i])
	{
		i++;
	}
	tab = malloc(i * sizeof(char));
	if (tab == NULL)
		return (0);
	while (src[j] != '\0')
	{
		tab[j] = src[j];
		j++;
	}
	tab[j] = '\0';
	return (tab);
}
